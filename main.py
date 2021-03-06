import tgl

#Import commands
import importdir
importdir.do("commands", globals())
importdir.get_names("commands")
module_list = importdir.module_list

tgl.PEER_USER = 1
tgl.PEER_CHAT = 2
tgl.PEER_ENCR_CHAT = 4

allow_messages = False
bot_id = ""


def on_binlog_replay_end():
	"This is called when replay of old events end. Any updates prior this call were already received by this client some time ago."
	
def on_get_difference_end():
	"This is called after first get_difference call. So we received all updates after last client execute."
	#Finished launching, allowing commands now
	global allow_messages
	allow_messages = True
	
def on_our_id(our_id):
	"Informs about id of currently logged in user."
	global bot_id
	bot_id = our_id
	
def on_msg_receive(msg):
	"This is called when we receive new tgl.Msg object (may be called before on_binlog_replay_end, than it is old msg)."
	global bot_id
	if allow_messages == True and msg.src.id != bot_id:
		if msg.text == None:
			return
		replyTo = '' #Work out where to send our reply
		if msg.dest.id == bot_id: #Private chats reply to the user
			replyTo = msg.src
		else: #Group chats reply to the group
			replyTo = msg.dest		
		#Check if this message is calling a system command
		words = msg.text.split()
		if words[0].lower() == "!help": #Execute help command
			if len(words) == 1: #If only one word aka '!help', send help command
				send_help(replyTo)
			else: #If several words, send specific help command
				send_command_help(replyTo, words[1].lower())
			return
		if words[0].lower() == "!reload": #Execute reload command
			if words[1]:
				reload_module(replyTo, words[1])
				return
		for i in module_list:
			if globals()[i].will_respond_to_msg(msg.text): #Check if module will respond to this msg
					globals()[i].run_command(replyTo, msg.text, msg.src) #Run the main command of that module
			
def on_user_update(peer, what_changed):
	"Updated info about user. peer is a tgl.Peer object representing the user, and what_changed is array of strings."


def on_chat_update(peer, what_changed):
	"Updated info about chat. peer is a tgl.Peer object representing the chat, and what_changed is array of strings."


def on_secret_chat_update(peer, what_changed):
	"Updated info about secret chat. peer is a tgl.Peer object representing the secret chat, and what_changed is array of strings."

tgl.set_on_binlog_replay_end(on_binlog_replay_end)
tgl.set_on_get_difference_end(on_get_difference_end)
tgl.set_on_our_id(on_our_id)
tgl.set_on_msg_receive(on_msg_receive)
tgl.set_on_secret_chat_update(on_secret_chat_update)
tgl.set_on_user_update(on_user_update)
tgl.set_on_chat_update(on_chat_update)
	
def reload_module(replyTo, module):
	"Reloads a module"
	global module_list
	for i in module_list:
		if i == module:
			reload(globals()[i])
			replyTo.send_msg(i + " reloaded")
			return
	replyTo.send_msg("No command by that name")
	
	
def send_help(replyTo):
	"Sends help message"
	response = "Novaso Telegram Bot v2.0\n\nLoaded commands:"
	global module_list
	for i in module_list:
		response = response + "\n" + globals()[i].command_name + " - " + globals()[i].short_description
	response = response + '\n\n!help <command> to get help for that command'
	replyTo.send_msg(response)

def send_command_help(replyTo, command):
	"Sends help message about a specific command"
	global module_list
	for i in module_list:
		if i == command:
			response = globals()[i].long_description
			replyTo.send_msg(response)
			return
	replyTo.send_msg("No command by that name")