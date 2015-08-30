command_name = "Ping"
short_description = "Returns pong"

def will_respond_to_msg(text):
	words = text.split()
	if words[0].lower() == "!ping":
		print True #debug
		return True
	else:
		print False #debug
		return False

def run_command(replyTo, text):
	"Returns pong"
	replyTo.send_msg("Pong")