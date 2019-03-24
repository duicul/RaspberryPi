#!/usr/bin/python
import sys
import RPi.GPIO as GPIO

pin=sys.argv[1]
print("pin for PIR "+str(pin))
GPIO.setup(pin, GPIO.IN)

def callback_pin(channel):
    print("pin activated")

GPIO.add_event_detect(pin, GPIO.RISING)
GPIO.add_event_callback(pin,callbackpin)

sensor = Adafruit_DHT.DHT22

while(True):
    pass

GPIO.cleanup()

