import requests
import json
import time

def getdata():
	r = requests.post('http://192.168.1.38:8765/outputpins',"outputpins")
    	return r.text
