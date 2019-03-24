#!/usr/bin/python
import sys
import RPi.GPIO as GPIO


pin=int(sys.argv[1])
print("pin for PIR "+str(pin))
GPIO.setmode(GPIO.BOARD)
GPIO.setup(pin, GPIO.IN,pull_up_down=GPIO.PUD_DOWN)

def callback_pin(channel):
    print("pin activated")

GPIO.add_event_detect(pin, GPIO.RISING)
GPIO.add_event_callback(pin,callback_pin)

while(True):
    pass

GPIO.cleanup()

