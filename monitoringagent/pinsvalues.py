import re
import hashlib
import json

class Pins:
    def __init__(self,file_inp,file_ext):
        self.file_inp=file_inp
        self.file_ext=file_ext

    def getInPins(self):
        with open(self.file_inp) as json_data:
            d = json.load(json_data)
            json_data.close()
            return d
    
    def getOutPins(self):
        with open(self.file_ext) as json_data:
            d = json.load(json_data)
            json_data.close()
            return d
        
    def setInPins(self,in_pins):
        with open(self.file_inp, 'w') as infile:
            json.dump(in_pins,infile)

    def setOutPins(self,out_pins):
        with open(self.file_ext, 'w') as outfile:
            json.dump(out_pins,outfile)

    def resetInPins(self):
        with open(self.file_inp, 'w') as infile:
            json.dump({},infile)

    def resetOutPins(self):
        with open(self.file_ext, 'w') as outfile:
            json.dump({},outfile)
    

if __name__ == '__main__':
    p=Pins('in_pins.json','out_pins.json')
    p.resetInPins()
    p.resetOutPins()
    p.setOutPins({'1':True,'2':False})
    print(str(p.getOutPins()))
