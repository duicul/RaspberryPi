import sys
from gpiozero import LED
from time import sleep

print(sys.argv)
pin=int(sys.argv[1])
val=sys.argv[2]
led = LED(pin)
if val=="off" :
    led.off()
elif val=="on" :
    led.on()
else : print("option unknown")
