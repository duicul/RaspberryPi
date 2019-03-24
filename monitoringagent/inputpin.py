import sys
import Adafruit_DHT

def readDHT11(pin):
    sensor=Adafruit_DHT.DHT11
    humidity, temperature = Adafruit_DHT.read_retry(sensor, pin)
    return (humidity,temperature)

def readDHT22(pin):
    sensor=Adafruit_DHT.DHT22
    humidity, temperature = Adafruit_DHT.read_retry(sensor, pin)
    return (humidity,temperature)

if __name__ == "__main__":
    print('Test')
