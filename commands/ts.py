command_name = "Teamspeak"
short_description = "Who is on teamspeak?"
long_description = "Teamspeak Command - v1.0 \nUsage: !ts \nReturns a list of people on the teamspeak server'"

import socket
	
def will_respond_to_msg(text):
	words = text.split()
	if words[0].lower() == "!ts":
		return True
	else:
		return False

def run_command(replyTo, text):
	"Returns a list of people on the teamspeak server"
	
	server = socket.connect('localhost', 10011)
	QueryState = {
		Off = 0,
		Init = 1,
		LoggedIn = 2,
		OnServer = 3,
		GotUsers = 4,
		GotChannels = 5,
		LoggedOut = 6
	}
	currentState = QueryState.Off
	successMsg = "error id=0 msg=ok"
	clientList = ""
	channelList = ""
	
	while True:
	response = server:receive('*l')

	if currentState == QueryState.Off and response == 'TS3':
		currentState = QueryState.Init
		server:send('login ' .. data.username .. ' ' .. data.password .. '\n')
	elseif currentState == QueryState.Init and response == successMsg:
		currentState = QueryState.LoggedIn
		server:send('use port=9987\n')
	elseif currentState == QueryState.LoggedIn and response == successMsg:
		currentState = QueryState.OnServer
		server:send('clientlist -voice\n')
	elseif currentState == QueryState.OnServer and response ~= successMsg:
		clientList = clientList .. response
	elseif currentState == QueryState.OnServer and response == successMsg:
		currentState = QueryState.GotUsers
		server:send('channellist\n')
	elseif currentState == QueryState.GotUsers and response ~= successMsg:
		channelList = channelList .. response
	elseif currentState == QueryState.GotUsers and response == successMsg:
		currentState = QueryState.GotChannels
		server:send('logout\n')
	elseif currentState == QueryState.GotChannels and response == successMsg:
		currentState = QueryState.LoggedOut
		server:send('quit\n')
	elseif currentState == QueryState.LoggedOut and response == successMsg:
		currentState = QueryState.Off
		server:close()
		break
		
	users = {}