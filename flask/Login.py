from flask import Flask,session, redirect, url_for, request,render_template
import configvalue
#from gpiozero import LED
from time import sleep
#import Adafruit_DHT
import myloginstatus
import data_retr

app = Flask(__name__)
app.secret_key = '571ba9$#/~90'

@app.route('/data_retr')
def data_status():
	return "okay stubbed" #data_retr.showdata()

@app.route('/success/<name>')
def success(name):
   return 'welcome %s' % name

@app.route('/loginstatus.py')
def loginstatus():
	return myloginstatus.show()

@app.route('/login',methods = ['POST', 'GET'])
def login():
   if request.method == 'POST':
      session['username'] = request.form['nm'] 
      return redirect('/')
   else:
      sessiom['username'] = request.args.get('nm')
      return redirect('/')

@app.route('/')
def index():
	if 'username' in session:
		username = session['username']
	else:   username="anonymous"
	return render_template('login.html',name=username)

@app.route('/on')
def turnon():
	LED(47).on()

@app.route('/getconfigdata')
def getdata():
	return configvalue.getconfigdata("../config.txt")

@app.route('/setconfigdata')
def setdata():
        if request.method == 'POST':
                user = request.form['user']
                password = request.form['pass']
                ip = request.form['ip']
                port = request.form['port']
                configvalue.setconfigdata(user,password,ip,port)

@app.route('/board_status')
def board_status():
	return 'temperature humidity pin settings'	

@app.route('/off')
def turnoff():
	LED(47).off()

@app.route('/logout')
def logout():
	session.pop('username',None)
	return redirect('/')

if __name__ == '__main__':
   app.run(debug = True,host='0.0.0.0')


#def read_temp(pin):
#	sensor = Adafruit_DHT.DHT11
#	humidity, temperature = Adafruit_DHT.read_retry(sensor, pin)
#	print(str(humidity)+"  "+str(temperature))

