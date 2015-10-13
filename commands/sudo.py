command_name = "Sudo"
short_description = "Sudo Command"
long_description = "Sudo Command - v1.1\n\nUsage: \n!sudo kick <username> \nKicks the user from the group \n\n!sudo invite <username> \nInvites the user to the group \n\n!sudo list \nLists userinfo of everyone in the group "



def will_respond_to_msg(text):
	words = text.split
	if words[0].lower() == "!sudo":
		return True
	else:
		return False

def run_command(replyTo, text, src):
	"Runs sudo commands"
	#Reset variables
	username = ""

	
	