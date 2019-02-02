import requests
import json
import time
import sys
import random
from extractvalues import Extractdata_Config,Insertdata_Config
loop=0
#user="duicul"
#password="daniel"
#ip = sys.argv[1] if len(sys.argv)>1 else 'localhost'
#port = sys.argv[2] if len(sys.argv)>2 else 8765
#refresh_in=30
#refresh_out=1
try:
    while(True):
        print("Loop "+str(loop))
        loop=loop+1
        time.sleep(1)
        ed=Extractdata_Config("../config.txt")
        insd=Insertdata_Config("../config.txt")
        user=ed.getUsername()
        password=ed.getPassword()
        ip=ed.getIp()
        port=ed.getPort()
        refresh_in=int(ed.getRefresh_In())
        refresh_out=int(ed.getRefresh_Out())
        if loop<refresh_in and loop>=refresh_out:
            pins_dict={}
            pins_dict['data']="outputpins"
            pins_dict['user']=user
            pins_dict['password']=password
            addr='http://'+str(ip)+":"+str(port)+"/outputpinsstatus"
            print(addr)
            r = requests.post(addr,json.dumps(pins_dict))
            print(r.text)
            y=json.loads(r.text)
            print(y)
            for i in range(21):
                try:
                    print(str(i)+"  "+str(y[str(i)]))
                except KeyError:
                    pass
                    #print("Not received "+str(i))
        elif loop>=refresh_in :
            loop=0
            pins_dict={}
            pins_dict['data']="pins"
            pins_dict['user']=user
            pins_dict['password']=password
            addr='http://'+str(ip)+":"+str(port)+"/pinsstatus"
            print(addr)
            r = requests.post(addr,json.dumps(pins_dict))
            print(r.text)
            y=json.loads(r.text)
            in_pins=json.loads(y['IN'])
            out_pins=json.loads(y['OUT'])
            print(y)
            print(in_pins)
            print(out_pins)
            inpins_list=[]
            for i in range(21):
                try:
                    print(str(i)+"  "+str(in_pins[str(i)]))
                    inpins_list.append([str(i),str(in_pins[str(i)])])        
                except KeyError:
                    try:
                        print(str(i)+"  "+str(out_pins[str(i)]))
                    except KeyError:
                        pass
			#print("Not received "+str(i))
            pins_dict={}
            pins_dict['data']="inputpins"
            pins_dict['user']=user
            pins_dict['password']=password
            for i in inpins_list:
                pins_dict[i[0]]=random.random()*40
            data=json.dumps(pins_dict)
            addr='http://'+str(ip)+":"+str(port)+"/inputpinsstatus"
            print(addr)
            r = requests.post(addr,data)
except Exception as e:
    print("Main server is down")
    print(e)
