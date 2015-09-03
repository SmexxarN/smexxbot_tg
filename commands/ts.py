command_name = "Teamspeak"
short_description = "Who is on teamspeak?"
long_description = "Teamspeak Command - v1.0 \nUsage: !ts \nReturns a list of people on the teamspeak server"

import socket
import re
	
def will_respond_to_msg(text):
	words = text.split()
	if words[0].lower() == "!ts":
		return True
	else:
		return False

def run_command(replyTo, text):
	"Returns a list of people on the teamspeak server"
	
	server = socket.connect("localhost", 10011)
	class QueryState:
		Off = 0
		Init = 1
		LoggedIn = 2
		OnServer = 3
		GotUsers = 4
		GotChannels = 5
		LoggedOut = 6

	currentState = QueryState.Off
	successMsg = "error id=0 msg=ok"
	clientList = ""
	channelList = ""
	
	while True:
		response = server:receive("*l")

		if currentState == QueryState.Off and response == "TS3":
			currentState = QueryState.Init
			server:send("login " .. data.username .. " " .. data.password .. "\n")
		elseif currentState == QueryState.Init and response == successMsg:
			currentState = QueryState.LoggedIn
			server:send("use port=9987\n")
		elseif currentState == QueryState.LoggedIn and response == successMsg:
			currentState = QueryState.OnServer
			server:send("clientlist -voice\n")
		elseif currentState == QueryState.OnServer and response != successMsg:
			clientList = clientList .. response
		elseif currentState == QueryState.OnServer and response == successMsg:
			currentState = QueryState.GotUsers
			server:send("channellist\n")
		elseif currentState == QueryState.GotUsers and response != successMsg:
			channelList = channelList .. response
		elseif currentState == QueryState.GotUsers and response == successMsg:
			currentState = QueryState.GotChannels
			server:send("logout\n")
		elseif currentState == QueryState.GotChannels and response == successMsg:
			currentState = QueryState.LoggedOut
			server:send("quit\n")
		elseif currentState == QueryState.LoggedOut and response == successMsg:
			currentState = QueryState.Off
			server:close()
			break
		
	users = {}
	for user in re.match("[^|]+", clientList):	
		newUser = {}
		for k, v in re.match("([^%s]+)=([^%s]+)", user):
			print(k, v)
			newUser[k] = v
		if newUser.client_typ == "0":
			users.append(newUser)
		elseif newUser.client_type == "1":
			savedId = newUser.cid
	
	channels = {}
	for channel in re.match("[^|]+", channelList):
		newChannel = {}
		for k, v in re.match("([^%s]+)=([^%s]+)", channel):
			print(k, v)
			newChannel[k] = v
		channels.append(newChannel)

	response = ""

	if len(users) == 0:
		response = "There is nobody on TeamSpeak."
	elseif len(users) == 1:
		response = "There is 1 person on TeamSpeak:"
	else:
		response = "There are " .. len(users) .. " people on TeamSpeak:"

	for i = 1, len(channels):
		if channels[i].total_clients != "0":
			channelname = re.sub(channels[i].channel_name, "\\s", " ")
			channels[i].users = {}
	
	for i = 1, len(users):
		nickname = re.sub(users[i].client_nickname, "\\s", " ")
		for j = 1, len(channels):
			if channels[j].cid == users[i].cid:
				channels[j].users.append(nickname)

	
	for i = 1, len(channels):
		if channels[i].total_clients == "1" and channels[i].cid == savedId:
		elseif channels[i].total_clients != "0":
			local channelname = string.gsub(channels[i].channel_name, "\\s", " ")
			response = response .. "\n" .. channelname
			for j = 1, len(channels[i].users):
				response = response .. "\n" .. "\t---" .. channels[i].users[j]
	send_msg(replyTo, response, ok_cb, False)
