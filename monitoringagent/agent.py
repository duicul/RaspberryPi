import requests
import json
import time
loop=0
while(loop<100):
    print("Loop "+str(loop))
    data="outputpins"
    r = requests.post('http://192.168.1.38:8765/outputpins',data)
    print(r.text)
    y=json.loads(r.text)
    print(y)
    for i in range(21):
        try:
            print(str(i)+"  "+y[str(i)])
        except KeyError:
            print("Not received "+str(i))
    loop=loop+1
    time.sleep(1.2)
