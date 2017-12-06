#!/usr/bin/python

import sys
import time
import random
import signal
import subprocess
import datetime
import telepot
import os
#import RPi.GPIO as GPIO

#GPIO.setwarnings(False)
# to use Raspberry Pi board pin numbers
#GPIO.setmode(GPIO.BOARD)
# set up GPIO output channel
#GPIO.setup(40, GPIO.OUT)

# send terminal command and deliver output to chat telegram
def run_command(commandt):
    p = subprocess.Popen(commandt,
                        stdout=subprocess.PIPE,
                        stderr=subprocess.STDOUT)
    return iter(p.stdout.readline, b'')

def handle(msg):
    chat_id = msg['chat']['id']
    command = msg['text']
    print 'Got command: %s' % command

    # if command == 'On':
    #    bot.sendMessage(chat_id, text="Light ON")
    #    GPIO.output(40,GPIO.HIGH)
    #    return;
    # elif command == 'Off':
    #    bot.sendMessage(chat_id, text="Light OFF")
    #    GPIO.output(40,GPIO.LOW)
    #    return;
    if command == 'Hai':
        hai_text = '''Hai Nayirpro!'''
        bot.sendMessage(chat_id, hai_text)
    elif command == 'Trace':
        commandt = 'traceroute 8.8.8.8'.split()
        for line in run_command(commandt):
            bot.sendMessage(chat_id, line)
    elif command == 'Woi':
        bot.sendMessage(chat_id, "Siap! Laksanakan!")
    elif command == 'Kepre':
        aip = os.system("ping -c 1 192.168.10.11")
        if aip == 0:
            bot.sendMessage(chat_id, text="A Up!")
        else:
            bot.sendMessage(chat_id, text="A Down!")
        bip = os.system("ping -c 1 192.168.10.12")
        if bip == 0:
            bot.sendMessage(chat_id, text="B Up!")
        else:
            bot.sendMessage(chat_id, text="B Down!")
        cip = os.system("ping -c 1 192.168.10.13")
        if cip == 0:
            bot.sendMessage(chat_id, text="C Up!")
        else:
            bot.sendMessage(chat_id, text="C Down!")
    else:
        pass
            
bot = telepot.Bot('000000000:AAA_AA-XXXXXXXXXXXXXXXXXXXXXXXXXXXX')
bot.message_loop(handle)
print 'I am listening...'

while 1:
     time.sleep(10)
