#!/usr/bin/env python

from __future__ import print_function
import sys
import threading

import time
import json

from satori.rtm.client import make_client, SubscriptionMode

channel = "NWS-All-USA-Alerts"
endpoint = "wss://open-data.api.satori.com"
appkey = "DBC51f5a70D2dC4bfAE1CC4D6E7dbdC9"

weather_op = "weather_updates.txt"
weather_messages = "weather_msg_summary.txt"

updates = []

while(True):
    with make_client(
            endpoint=endpoint, appkey=appkey) as client:
        print('Connected!')

        mailbox = []
        got_message_event = threading.Event()

        class SubscriptionObserver(object):
            def on_subscription_data(self, data):
                for message in data['messages']:
                    mailbox.append(message)
                got_message_event.set()

        subscription_observer = SubscriptionObserver()
        client.subscribe(
            channel,
            SubscriptionMode.SIMPLE,
            subscription_observer)


        if not got_message_event.wait(10):
            print("Timeout while waiting for a message")
##            sys.exit(1)

        for message in mailbox:
            updates = message["title"] + ": \t " + message["summary"] + "\n\n--\n\n"
            
            with open(weather_op, "a") as weather_file:
                message = json.dumps(message) + "\n\n------\n\n"
                weather_file.write(message)
            with open(weather_messages, "a") as weather_summary:
                weather_summary.write(updates)
                
            print('Got message "{0}"'.format(message))

    time.sleep(10)


if __name__ == '__main__':
    main()