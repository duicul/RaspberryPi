#!/usr/bin/python
import Adafruit_DHT
import sys
sensor = Adafruit_DHT.DHT11

pin = int(sys.argv[1])
print("Pin "+str(pin))
humidity, temperature = Adafruit_DHT.read_retry(sensor, pin)

print(str(temperature)+" "+str(humidity))

if humidity is not None and temperature is not None:

    print('Temp={0:0.1f}*C  Humidity={1:0.1f}%'.format(temperature, humidity))

else:

    print('Failed to get reading. Try again!')
