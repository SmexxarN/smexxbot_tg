command_name = "Sudo"
short_description = "Sudo Command"
long_description = "Sudo Command - v1.1\n\nUsage: \n!sudo kick <username> \nKicks the user from the group \n\n!sudo invite <username> \nInvites the user to the group \n\n!sudo list \nLists userinfo of everyone in the group "

chatinforesponse = ""
replyTo2 = nil
listofstarts = {}
userinfostring = ""
user = ""
sendlist = false

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
	
	for i in range(0, len(admins):
		if admins[i] == username:
			return true


def module.init():
	print "Module init"
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

def module.will_respond_to_msg(msg):
	words = {}
	for word in string.gmatch(msg.text, "%S+"):
		words[len(words) + 1] = string.lower(word);
	return string.lower(words[1]) == "!sudo"

def module.on_msg_receive(msg, replyTo):
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
		else:
			id = words[3] #Set the userid to votekick
		
		
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
