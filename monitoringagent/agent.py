import requests
import json
import time
import sys
loop=0
ip = sys.argv[1] if len(sys.argv)>1 else 'localhost'
port = sys.argv[2] if len(sys.argv)>2 else 8765
try:
    while(loop<100):
        print("Loop "+str(loop))
        loop=loop+1
        time.sleep(1.2)
        if loop<30:
            data="outputpins"
            addr='http://'+str(ip)+":"+str(port)+"/outputpinsstatus"
            print(addr)
            r = requests.post(addr,data)
            print(r.text)
            y=json.loads(r.text)
            print(y)
            for i in range(21):
                try:
                    print(str(i)+"  "+str(y[str(i)]))
                except KeyError:
                    print("Not received "+str(i))
        else :
            loop=0
            data="pins"
            addr='http://'+str(ip)+":"+str(port)+"/pinsstatus"
            print(addr)
            r = requests.post(addr,data)
            print(r.text)
            y=json.loads(r.text)
            in_pins=json.loads(y['IN'])
            out_pins=json.loads(y['OUT'])
            print(y)
            print(in_pins)
            print(out_pins)
            for i in range(21):
                try:
                    print(str(i)+"  "+str(in_pins[str(i)]))
                except KeyError:
                    try:
                        print(str(i)+"  "+str(out_pins[str(i)]))
                    except KeyError:
                        print("Not received "+str(i))
except ConnectionError:
    print("Main server is down")
