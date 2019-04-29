import sys
import Adafruit_DHT
import RPi.GPIO as GPIO


class InputPin:
    pir_list=[]
    
    def sendpirdata(channel):
        ed=Extractdata_Config("../config.txt")
        user=ed.getUsername()
        ip=ed.getIp()
        port=ed.getPort()
        addr='http://'+str(ip)+":"+str(port)+"/pirpins"
        pir_dict={}
        pir_dict['data']="pirpin"
        pir_dict['user']=user
        pir_dict['pin_no']=channel
        data=json.dumps(pins_dict)
        r = requests.post(addr,data)
        print("send pir data "+str(channel)+" "+str(data))

    def set_pir_pins(pir_pin_list):
        print("pir pins received "+str(pir_pin_list))
        pins_to_remove=list(set(pir_list)-set(pir_pin_list))
        pins_to_add=list(set(pir_pin_list)-set(pir_list))
        print("current pin list "+str(pir_list))
        print("pirpins to add "+str(pins_to_add))
        print("pirpins to remove"+str(pins_to_remove))
        pir_list=pir_list+pins_to_add
        for i in pins_to_remove:
            pir_list.remove(i)
            GPIO.remove_event_detect(int(i))
            GPIO.cleanup(int(i))
        for i in pins_to_add:
            GPIO.setup(int(i), GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
            GPIO.add_event_detect(int(i), GPIO.RISING, callback=sendpirdata, bouncetime=200)

    def readDHT11(pin):
        sensor=Adafruit_DHT.DHT11
        humidity, temperature = Adafruit_DHT.read_retry(sensor, pin)
        return (temperature,humidity)

    def readDHT22(pin):
        sensor=Adafruit_DHT.DHT22
        humidity, temperature = Adafruit_DHT.read_retry(sensor, pin)
        return (temperature,humidity)
