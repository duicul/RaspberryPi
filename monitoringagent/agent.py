#!/usr/bin/env python
import requests
import json
import time
import sys
import random
import traceback
from extractvalues import Extractdata_Config,Insertdata_Config
from outputpin import outputpinon,outputpinoff
from inputpin import InputPin
from pinconfig import pin_to_GPIO,GPIO_to_pin
import RPi.GPIO as GPIO
loop1=0
loop2=0


#all pin numbers from protocol are GPIO
pininput=InputPin()
init = True
try:
    while(True):
        print("Loop "+str(loop1)+" "+str(loop2))
        loop1=loop1+1
        loop2=loop2+1
        ed=Extractdata_Config("../config.txt")
        insd=Insertdata_Config("../config.txt")
        user=ed.getUsername()
        ip=ed.getIp()
        port=ed.getPort()
        refresh_in=int(ed.getRefresh_In())
        refresh_out=int(ed.getRefresh_Out())
        logtime=int(ed.getLogTime())
        time.sleep(1)
        if loop1>=refresh_out or init:
            loop1=0
            pins_dict={}
            pins_dict['data']="outputpins"
            pins_dict['user']=user
            addr='http://'+str(ip)+":"+str(port)+"/outputpinsstatus"
            r = requests.post(addr,json.dumps(pins_dict))
            print(r.text)
            y=json.loads(r.text)
            print(y)
            outpins=[]
            print("First method")
            for pin in y :
                print("pin "+pin+"  value "+str(y[pin]))
                if y[pin]== 1:
                        outputpinon(GPIO_to_pin(int(pin)))
                else :
                        outputpinoff(GPIO_to_pin(int(pin)))
            print("okay")
            '''print("Second method")
            for i in range(1,27):
                try:
                    print(str(i)+"  "+str(y[str(i)]))
                    if y[str(i)]== 1:
                        outputpinon(GPIO_to_pin(int(i)))
					else :
                        outputpinoff(GPIO_to_pin(int(i)))
				except KeyError:
                    pass
                    #print("Not received "+str(i))'''
        if loop2>=refresh_in or init:
            loop2=0
            pins_dict={}
            pins_dict['data']="pins"
            pins_dict['user']=user
            addr='http://'+str(ip)+":"+str(port)+"/pinsstatus"
            r = requests.post(addr,json.dumps(pins_dict))
           # print(r.text)
            y=json.loads(r.text)
            in_pins=json.loads(y['IN'])
            #out_pins=json.loads(y['OUT']) no outpins sent
            #print(y)
            print(in_pins)
            #print(out_pins) no outpins sent
            in_pins=json.loads(y['IN'])
            inpins_list=[]
            for in_pin in in_pins :
                inpins_list.append([str(in_pin),str(in_pins[in_pin])])
            '''for i in range(1,27):
                try:
                    #print(str(i)+"  "+str(in_pins[str(i)]))
                    inpins_list.append([str(i),str(in_pins[str(i)])])        
                except KeyError:
                    try:
                        print(str(i)+"  "+str(out_pins[str(i)]))
                    except KeyError:
                        pass
			#print("Not received "+str(i))'''
            pins_dict={}
            pins_dict['data']="inputpins"
            pins_dict['user']=user
            pins_dict['logtime']=logtime
            pir_list=[]
            data_dict={}
            print(inpins_list)
            for i in inpins_list:
                print(i)
                if i[1]=="DHT11": #daca senzorul este DHT11
                    val=pininput.readDHT11(int(i[0])) #citire valoare senzor
                    if val[0] != None and val[1] != None: #daca valoarea a fost citita
                        data_dict[i[0]]=str(val[0])+" "+str(val[1])#este creat un dictionar 
								   #cu valorile senzorilor
                elif i[1]=="DHT22": #daca senzorul este DHT11
                    val=pininput.readDHT22(int(i[0])) #citire valoare senzor
                    print(val)
                    if val[0] != None and val[1] != None: #daca valoarea a fost citita
                        data_dict[i[0]]=str(val[0])+" "+str(val[1])#este creat un dictionar 
                                                                    #cu valorile senzorilor
                elif i[1]=="PIR": #daca senzorul este PIR
                    pir_list.append(i[0])  #stocare valoare pin pentru cereri asincrone               
            pins_dict['in_pins']=data_dict #este adaugat in JSON dictionarul cu valorile pinilor de intrare
            #print(pins_dict)
            pininput.set_pir_pins(map(GPIO_to_pin,pir_list)) #stocare pini senzori PIR
            data=json.dumps(pins_dict) #creare JSON pe baza dictionarului de pini
            addr='http://'+str(ip)+":"+str(port)+"/inputpinsstatus" #adresa server din config.txt
            r = requests.post(addr,data) #trimitere cerere
        init = False
    GPIO.cleanup()
except Exception as e:
    GPIO.cleanup()
    print("Main server is down")
    print(traceback.format_exc())
