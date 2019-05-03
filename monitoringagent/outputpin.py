import sys
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BOARD)

def outputpinon(pin):
    GPIO.cleanup(pin)
    GPIO.setup(pin, GPIO.OUT)
    GPIO.output(pin, True)

def outputpinoff(pin):
    GPIO.cleanup(pin)
    GPIO.setup(pin, GPIO.OUT)
    GPIO.output(pin, False)

if __name__ == "__main__":
    print(sys.argv)
    pin=int(sys.argv[1])
    val=sys.argv[2]
    if val=="off" :
        outputpinoff(pin)
    elif val=="on" :
        outputpinon(pin)
    else : print("option unknown")
    while(True):
          pass
    GPIO.cleanup()
