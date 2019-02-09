import re
import time
import json
import psutil
from slackclient import SlackClient


#Below declares the Bot's id
slack_client = SlackClient("xoxb-544307237201-547827349335-djslFYZWEp5QG0iZd4ML9FyL")


#Fetch the Bot's User ID
user_list = slack_client.api_call("users.list")
for user in user_list.get('members'):
    if user.get('name') == "prisonmikebot":
        slack_user_id = user.get('id')
        break


#Start connection
if slack_client.rtm_connect():
    print "Connected!"

    while True:
        time.sleep(1)
        #print slack_client.rtm_read()
        for message in slack_client.rtm_read():
            if 'text' in message or 'attachments' in message:

                print "Message received: %s" % json.dumps(message, indent=2)

