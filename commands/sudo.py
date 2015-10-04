command_name = "Sudo"
short_description = "Sudo Command"
long_description = "Sudo Command - v1.1\n\nUsage: \n!sudo kick <username> \nKicks the user from the group \n\n!sudo invite <username> \nInvites the user to the group \n\n!sudo list \nLists userinfo of everyone in the group "

import time
import threading

global numberofvotes_yes = 0
global numberofvotes_no = 0
chatinforesponse = ""
replyTo2 = nil
listofstarts = {}
userinfostring = ""
user = ""
sendlist = false
global vote_running = 0


#Userinfo2
phone = ""
print_name = ""
id = ""
first_name = ""
username = ""


def userinfo(info, start):
	return
	#if not start:
	#	start = 1
	#if start > string.len(info):
	#	return
	#else:
	#	a = info:find("%d:", start)
	#	if a ~= nil:
	#		table.insert(listofstarts, a)
	#		userinfo(chatinforesponse, a+1)
	#	else:
	#		userinfo2()



def userinfo2():
	return
	#subuserstring = ""
	#last = nil
	#words = {}
	#for _, value in pairs(listofstarts):
	#	if last ~= nil:
	#		subuserstring = chatinforesponse:sub(last, value)
	#		words = {}
	#		for word in string.gmatch(subuserstring, "%S+"):
	#			words[len(words) + 1] = string.lower(word)
	#		for i=1, len(words) do
	#			if words[i] == "phone:":
	#				phone = word[i+1]
	#			elif words[i] == "print_name:":
	#				print_name = word[i+1]
	#			elif words[i] == "id:":
	#				id = word[i+1]
	#			elif words[i] == "first_name:":
	#				first_name = word[i+1]
	#			elif words[i] == "username:":
	#				username = word[i+1]
	#			if words[i] == user:
	#				print("Found the user") #Debug message
	#				return
	#	last = value


def perm_check(username):

	admins = {"smexxarn", "dennip", "mowsh", "brunado"}
	
	for i in range(0, len(admins)):
		if admins[i] == username:
			return true

			

def vote_count(id, end):
	send_msg(replyTo, "Current vote count:\nYes: " + numberofvotes_yes + "\nNo: " + numberofvotes_no, ok_cb, false)
	if end == true:
		if numberofvotes_yes >= 3:
			chat_del_user(replyTo, "user#" + id, ok_cb, false)
			send_msg(replyTo, id + " was kicked", ok_cb, false)
		global vote_running = 0



#def module.init():
	#Nothing


def tprint (tbl, indent):
	return
	#if not indent:
	#	indent = 0
	#for k, v in pairs(tbl):
	#	formatting = string.rep("  ", indent) .. k .. ": "
	#	if type(v) == "table":
	#		chatinforesponse = chatinforesponse .. formatting .. "\n"
	#		tprint(v, indent+1)
	#	else:
	#		chatinforesponse = chatinforesponse .. formatting .. tostring(v) .. "\n"
	#print("tprint")#Debug


def cb_function(extra, success, result):
	if success:
		tprint(result)
		if sendlist:
			send_msg(replyTo2, chatinforesponse, ok_cb, false)
		else:
			userinfo(chatinforesponse)

def will_respond_to_msg(text):
	words = {}
	for word in string.gmatch(msg.text, "%S+"):
		words[len(words) + 1] = string.lower(word);
	return string.lower(words[1]) == "!sudo"

def run_command(replyTo, text):
	"Runs sudo commands"
	#Reset variables
	chatinforesponse = ""
	replyTo2 = replyTo
	listofstarts = {}
	userinfostring = ""
	sendlist = false
	user = ""
	phone = ""
	print_name = ""
	id = ""
	first_name = ""
	username = ""
	
	words = {}
    for word in string.gmatch(msg.text, "%S+"):
        words[len(words) + 1] = word;
    
	
	
	if words[2] == "kick": #If the !kick command is run
		if words[3] == nil: #No user specified
			send_msg(replyTo, "Please specify a user to kick", ok_cb, false)
			return
		else:
			user = words[3] # Set the user to kick
		
		chat_info(replyTo, cb_function, false)#Lookup all users
		#wait(5)
		#userinfo(chatinforesponse) #Run function using the string with all users information
		#Is now done in cb_function
		
		#Check if sender is admin
		if perm_check(string.lower(msg.from.username)):
			chat_del_user(replyTo, "user#" .. id, ok_cb, false) #Kick
		else:
			send_msg(replyTo, "You do not have sufficient permissions", ok_cb, false) #Sender doesn't have permission
		
	if words[2] == "votekick": #Votekick for regular users
		if words[3] == nil: #No user specified
			send_msg(replyTo, "Please specify a userid to invite", ok_cb, false)
			return
		elif words[3] == "yes":
			if vote_running = 1:
				global numberofvotes_yes = numberofvotes_yes + 1
				vote_count(id)
			else:
				send_msg(replyTo, "The current vote has ended", ok_cb, false)
		elif words[3] == "no":
			if vote_running = 1:
				global numberofvotes_no = numberofvotes_no + 1
				vote_count(id)
			else:
				send_msg(replyTo, "The current vote has ended", ok_cb, false)
		else:
			id = words[3] #Set the userid to votekick
		
		#Run the actual command
		t = Timer(180.0, vote_count)
		t.start() #After 180 seconds, vote_count() will be executed
		if vote_running = 1:
			send_msg(replyTo, "The current vote has not ended", ok_cb, false)
			return
		global vote_running = 1
		global numberofvotes_yes = 1 #Reset votes
		global numberofvotes_no = 0 #Reset votes
		send_msg(replyTo, msg.from.username + " has initiated a vote to kick \nReply with '!sudo votekick yes' to vote in favor of the kick \nReply with '!sudo votekick no' to vote against the kick" + words[3], ok_cb, false)
		
		
		
	if words[2] == "invite": #If the invite command is run
		if words[3] == nil: #No user specified
			send_msg(replyTo, "Please specify a userid to invite", ok_cb, false)
			return
		else:
			id = words[3] # Set the userid to invite

		#Check if sender is admin
		if perm_check(string.lower(msg.from.username)):
			chat_add_user(replyTo, "user#" .. id, ok_cb, false) #Invite
		else:
			send_msg(replyTo, "You do not have sufficient permissions", ok_cb, false) #Sender doesn't have permission

	
	if words[2] == "list": #If list command is run
		#chat_info("chat#25231397", cb_function, false)
		sendlist = true
		chat_info(replyTo, cb_function, false)


return module
