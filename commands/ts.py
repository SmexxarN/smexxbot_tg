command_name = "Teamspeak"
short_description = "Who is on teamspeak?"
long_description = "Teamspeak Command - v1.0 \nUsage: !ts \nReturns a list of people on the teamspeak server"

import socket
import re
import json
	
def will_respond_to_msg(text):
	words = text.split()
	if words[0].lower() == "!ts":
		return True
	else:
		return False

def run_command(replyTo, text):
	"Returns a list of people on the teamspeak server"
	
	with open('config.json') as data_file:    #Retrieve username and password
		data = json.load(data_file)
	
	HOST = "127.0.0.1"
	PORT = 10011
	
	server = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #Setup a new socket
	server.connect((HOST, PORT))
	
	class States:
		Off = 0
		Init = 1
		LoggedIn = 2
		OnServer = 3
		GotUsers = 4
		GotChannels = 5
		LoggedOut = 6
	
	QueryState = States()

	currentState = QueryState.Off
	successMsg = "error id=0 msg=ok"
	clientList = ""
	channelList = ""
	savedId = ""
	
	
	while True:
		response = server.recv()
		print response #debug

		if currentState == QueryState.Off and response == "TS3":
			currentState = QueryState.Init
			server.send("login " + data.username + " " + data.password + "\n")
		elif currentState == QueryState.Init and response == successMsg:
			currentState = QueryState.LoggedIn
			server.send("use port=9987\n")
		elif currentState == QueryState.LoggedIn and response == successMsg:
			currentState = QueryState.OnServer
			server.send("clientlist -voice\n")
		elif currentState == QueryState.OnServer and response != successMsg:
			clientList = clientList + response
		elif currentState == QueryState.OnServer and response == successMsg:
			currentState = QueryState.GotUsers
			server.send("channellist\n")
		elif currentState == QueryState.GotUsers and response != successMsg:
			channelList = channelList + response
		elif currentState == QueryState.GotUsers and response == successMsg:
			currentState = QueryState.GotChannels
			server.send("logout\n")
		elif currentState == QueryState.GotChannels and response == successMsg:
			currentState = QueryState.LoggedOut
			server.send("quit\n")
		elif currentState == QueryState.LoggedOut and response == successMsg:
			currentState = QueryState.Off
			server.close()
			break
		
	users = {}
	for user in re.match("[^|]+", clientList):	
		newUser = {}
		for k, v in re.match("([^%s]+)=([^%s]+)", user):
			print(k, v)
			newUser[k] = v
		if newUser.client_typ == "0":
			users.append(newUser)
		elif newUser.client_type == "1":
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
	elif len(users) == 1:
		response = "There is 1 person on TeamSpeak:"
	else:
		response = "There are " + len(users) + " people on TeamSpeak:"

	for i in range(1, len(channels)):
		if channels[i].total_clients != "0":
			channelname = re.sub(channels[i].channel_name, "\\s", " ")
			channels[i].users = {}
	
	for i in range(1, len(users)):
		nickname = re.sub(users[i].client_nickname, "\\s", " ")
		for j in range(1, len(channels)):
			if channels[j].cid == users[i].cid:
				channels[j].users.append(nickname)

	
	for i in range(1, len(channels)):
		if channels[i].total_clients != "0":
			if channels[i].cid == savedId:
				return
			channelname = string.gsub(channels[i].channel_name, "\\s", " ")
			response = response + "\n" + channelname
			for j in range(1, len(channels[i].users)):
				response = response + "\n" + "\t---" + channels[i].users[j]
	send_msg(replyTo, response, ok_cb, False)
