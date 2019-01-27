import extractvalues
def getconfigdata(filename):
    ed=extractvalues.Extractdata_Config("../config.txt")
    data="<p>"
    data = data +"Username: "+"<input id=\"username\" type=\"text\" value=\"+str(ed.getUsername())+\"> <br>"
    data = data +"Password: "+"<input id=\"password\" type=\"password\" value=\"+str(ed.getPassword())+\"> <br>"
    data = data +"IP: "+"<input id=\"ip\" type=\"text\" value=\"+str(ed.getIp())+\"> <br>"
    data = data +"IP: "+"<input id=\"port\" type=\"text\" value=\"+str(ed.getPort())+\"> <br>"
    data = data +"</p>"
    return data

def setconfigdata(username,password,ip,port):
    insd=extractvalues.Insertdata_Config("../config.txt")
    insd.setUsername(username)
    insd.setPassword(password)
    insd.setIp(ip)
    insd.setPort(port)

