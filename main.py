allow_messages = false
bot_id = ""

#import tgl

def test():
	print "test"

def tgl.on_binlog_replay_end():
	"This is called when replay of old events end. Any updates prior this call were already received by this client some time ago."
	return;

def tgl.on_get_difference_end():
	"This is called after first get_difference call. So we received all updates after last client execute."
	#Finished launching, allowing commands now
	allow_messages = True
	return;
	
def tgl.on_our_id(our_id):
	"Informs about id of currently logged in user."
	bot_id = our_id
	return;
	
def tgl.on_msg_receive(msg):
	"This is called when we receive new tgl.Msg object (may be called before on_binlog_replay_end, than it is old msg)."
	if allow_messages = True and msg.src != bot_id:
		if msg.text == nil:
			msg.text = 'none'
		replyTo #Work out where to send our reply
		if msg.dest.id == bot_id: #Private chats reply to the user
			replyTo = msg.src.name
		else: #Group chats reply to the group
			replyTo = msg.dest.name
		#Check if this message is calling a system command
		words = []
		for word in msg.text.split():
			words[len(words)+1] = word
		if words[0].lower() == "!help":
			#Execute help command
			#please finish
		if words[0].lower() == "!reload":
			#Execute reload command
			if words[1]:
				reload_module(replyTo, words[1])
				#please finish
				
	return;

def tgl.on_user_update(peer, what_changed):
	"Updated info about user. peer is a tgl.Peer object representing the user, and what_changed is array of strings."
	return;

def tgl.on_chat_update(peer, what_changed):
	"Updated info about chat. peer is a tgl.Peer object representing the chat, and what_changed is array of strings."
	return;

def tgl.on_secret_chat_update(peer, what_changed):
	"Updated info about secret chat. peer is a tgl.Peer object representing the secret chat, and what_changed is array of strings."
	return;
	
def reload_module(replyTo, module):
	return;
	
test()