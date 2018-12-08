from flask import Flask,session, redirect, url_for, request,render_template
from gpiozero import LED
from time import sleep
import Adafruit_DHT

app = Flask(__name__)
app.secret_key = '571ba9$#/~90'

@app.route('/success/<name>')
def success(name):
   return 'welcome %s' % name



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
		return "<font color=red size=20> Hello "+username+"</font>"+"<br><a href=\"/logout\"><button>Logout</button>"
	else:  return render_template('login.html')

@app.route('/on')
def turnon():
	LED(47).on()

@app.route('/off')
def turnoff():
	LED(47).off()

@app.route('/logout')
def logout():
	session.pop('username',None)
	return redirect('/')

if __name__ == '__main__':
   app.run(debug = True,host='0.0.0.0')


def read_temp(pin):
	sensor = Adafruit_DHT.DHT11
	print(humidity, temperature = Adafruit_DHT.read_retry(sensor, pin))
