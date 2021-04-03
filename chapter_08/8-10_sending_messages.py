# List containing series of short text messages
txt_msg_list = ['blahblahblah', 'imnotagossipbut', 'chatterchatterchatter']
snt_msgs = []

def show_messages(txt_msgs):
    """print each text message in list"""
    for txt_msg in txt_msgs:
        print(txt_msg)

def send_messages(txt_msgs):
    """ Print each text message and moves each message to sent_message list"""
    while txt_msgs:
        txt_msg = txt_msgs.pop()
        print(txt_msg)
        snt_msgs.append(txt_msg)

# Call send_messages() with copy of list of messages.
send_messages(txt_msg_lis)

# print both lists
print(txt_msg_list)
print(snt_msgs)