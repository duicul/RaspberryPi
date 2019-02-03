import sys
from gpiozero import LED
from time import sleep

def outputpinon(pin):
    led = LED(pin)
    led.on()

def outputpinoff(pin):
    led = LED(pin)
    led.off()

if __name__ == "__main__":
    print(sys.argv)
    pin=int(sys.argv[1])
    val=sys.argv[2]
    if val=="off" :
        outputpinoff(pin)
    elif val=="on" :
        outputpinon(pin)
    else : print("option unknown")
