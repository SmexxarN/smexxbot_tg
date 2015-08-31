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
	