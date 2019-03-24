import requests
import json
import time
import sys
import random
from extractvalues import Extractdata_Config,Insertdata_Config
from outputpin import outputpinon,outputpinoff
from inputpin import readDHT11,readDHT22
loop1=0
loop2=0

#set(a) - set(b) for motion pins not used anymore

#user="duicul"
#ip = sys.argv[1] if len(sys.argv)>1 else 'localhost'
#port = sys.argv[2] if len(sys.argv)>2 else 8765
#refresh_in=30
#refresh_out=1
try:
    while(True):
        print("Loop "+str(loop1)+" "+str(loop2))
        loop1=loop1+1
        loop2=loop2+1
        time.sleep(1)
        ed=Extractdata_Config("../config.txt")
        insd=Insertdata_Config("../config.txt")
        user=ed.getUsername()
        ip=ed.getIp()
        port=ed.getPort()
        refresh_in=int(ed.getRefresh_In())
        refresh_out=int(ed.getRefresh_Out())
        if loop1>=refresh_out:
            loop1=0
	    pins_dict={}
            pins_dict['data']="outputpins"
            pins_dict['user']=user
            addr='http://'+str(ip)+":"+str(port)+"/outputpinsstatus"
            print(addr)
            r = requests.post(addr,json.dumps(pins_dict))
            print(r.text)
            y=json.loads(r.text)
            print(y)
	    outpins=[]
            for i in range(40):
                try:
                    print(str(i)+"  "+str(y[str(i)]))
                    if y[str(i)]== 1:
	                print("outputpinon")
                        outputpinon(int(i))
		    else : outputpinoff(int(i))
		except KeyError:
                    pass
                    #print("Not received "+str(i))
        if loop2>=refresh_in :
            loop2=0
            pins_dict={}
            pins_dict['data']="pins"
            pins_dict['user']=user
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
            for i in range(40):
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
            for i in inpins_list:
                if i[1]=="DHT11":
                    pins_dict[i[0]]=readDHT11(i[0])[0]
                elif i[1]=="DHT22":
                    pins_dict[i[0]]=readDHT22(i[0])[0]
                else:
                    pins_dict[i[0]]=random.random()*40
            data=json.dumps(pins_dict)
            addr='http://'+str(ip)+":"+str(port)+"/inputpinsstatus"
            print(addr)
            r = requests.post(addr,data)
except Exception as e:
    print("Main server is down")
    print(e)
