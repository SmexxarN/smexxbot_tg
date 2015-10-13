command_name = "Sudo"
short_description = "Sudo Command"
long_description = "Sudo Command - v1.1\n\nUsage: \n!sudo kick <username> \nKicks the user from the group \n\n!sudo invite <username> \nInvites the user to the group \n\n!sudo list \nLists userinfo of everyone in the group "

import threading

numberofvotes_yes = 0
numberofvotes_no = 0
chatinforesponse = ""
replyTo2 = None
listofstarts = {}
userinfostring = ""
user = ""
sendlist = False
vote_running = 0


#Userinfo2
phone = ""
print_name = ""
id = ""
first_name = ""
username = ""


def userinfo(info, start):
	return
	

def userinfo2():
	return


def perm_check(username):

	admins = {"smexxarn", "dennip", "mowsh", "brunado"}
	
	for i in range(0, len(admins)):
		if admins[i] == username:
			return true

			

def vote_count(id, end):
	global numberofvotes_yes
	global numberofvotes_no
	global vote_running
	replyTo.send_msg("Current vote count:\nYes: " + numberofvotes_yes + "\nNo: " + numberofvotes_no)
	if end == true:
		if numberofvotes_yes >= 3:
			replyTo.del_user("user#" + id)
			replyTo.send_msg(id + " was kicked")
		vote_running = 0



def cb_function(extra, success, result):
	if success:
		tprint(result)
		if sendlist:
			send_msg(replyTo2, chatinforesponse, ok_cb, false)
		else:
			userinfo(chatinforesponse)

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

	
	