command_name = "Ping"
short_description = "Returns pong"
long_description = "Ping Command - v1.0 \nUsage: !ping \nReplies with 'Pong'"

def will_respond_to_msg(text):
	words = text.split()
	if words[0].lower() == "!ping":
		return True
	else:
		return False

def run_command(replyTo, text):
	"Returns pong"
	replyTo.send_msg("Pong")