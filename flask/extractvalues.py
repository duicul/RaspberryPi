import re
class Extractdata_Config:
    def __init__(self,file_name):
        self.file_name=file_name

    def getFile(self):
        file=open(self.file_name,'r')
        data=file.read()
        file.close()
        return data
    
    def getUsername(self):
        try:
            file=open(self.file_name,'r')
            data=file.read()
            found = re.search('username=(.*)', data).group(1)
            return found
        except AttributeError:
            return ''
        file.close()
            
    def getPassword(self):
        try:
            file=open(self.file_name,'r')
            data=file.read()
            found = re.search('password=(.*)', data).group(1)
            return found
        except AttributeError:
            return ''
        file.close()
        
    def getIp(self):
        try:
            file=open(self.file_name,'r')
            data=file.read()
            found = re.search('ip=(.*)', data).group(1)
            return found
        except AttributeError:
            return ''
        file.close()
        
    def getPort(self):
        try:
            file=open(self.file_name,'r')
            data=file.read()
            found = re.search('port=(.*)', data).group(1)
            return found
        except AttributeError:
            return ''
        file.close()

    def getRefresh_In(self):
        try:
            file=open(self.file_name,'r')
            data=file.read()
            found = re.search('refresh_in=(.*)', data).group(1)
            return found
        except AttributeError:
            return ''
        file.close()

    def getRefresh_Out(self):
        try:
            file=open(self.file_name,'r')
            data=file.read()
            found = re.search('refresh_out=(.*)', data).group(1)
            return found
        except AttributeError:
            return ''
        file.close()
        
class Insertdata_Config:
    def __init__(self,file_name):
        self.file_name=file_name

    def getFile_name(self):
        return self.file_name
    
    def setUsername(self,username):
        try:
            file=open(self.file_name,'r')
            data=file.read()
            file.close()
            file=open(self.file_name,'w')
            found = re.sub('username=.*', 'username=%s' % username,data)
            file.write(found)
        except AttributeError as e:
            print(e)
        file.close()
        
        
    def setPassword(self,password):
        try:
            file=open(self.file_name,'r')
            data=file.read()
            file.close()
            file=open(self.file_name,'w')
            found = re.sub('password=.*', 'password=%s' % password,data)
            file.write(found)
        except AttributeError:
            pass
        file.close()
        
    def setIp(self,ip):
        try:
            file=open(self.file_name,'r')
            data=file.read()
            file.close()
            file=open(self.file_name,'w')
            found = re.sub('ip=.*', 'ip=%s' % ip,data)
            file.write(found)
        except AttributeError:
            pass
        file.close()
        
    def setPort(self,port):
        try:
            file=open(self.file_name,'r')
            data=file.read()
            file.close()
            file=open(self.file_name,'w')
            found = re.sub('port=.*', 'port=%s' % port,data)
            file.write(found)
        except AttributeError:
            pass
        file.close()

    def setRefresh_In(self,refresh):
        try:
            file=open(self.file_name,'r')
            data=file.read()
            file.close()
            file=open(self.file_name,'w')
            found = re.sub('refresh_in=.*', 'refresh_in=%s' % refresh,data)
            file.write(found)
        except AttributeError:
            pass
        file.close()

    def setRefresh_Out(self,refresh):
        try:
            file=open(self.file_name,'r')
            data=file.read()
            file.close()
            file=open(self.file_name,'w')
            found = re.sub('refresh_out=.*', 'refresh_out=%s' % refresh,data)
            file.write(found)
        except AttributeError:
            pass
        file.close()

if __name__ == '__main__':
    ed=Extractdata_Config("config.txt")
    insd=Insertdata_Config("config.txt")
    print(ed.getFile())
    insd.setUsername("adas")
    insd.setPassword("pass")
    insd.setIp("31313")
    insd.setPort(6767)
    print(ed.getUsername())
    print(ed.getPassword())
    print(ed.getIp())
    print(ed.getPort())
