from flask import Flask,session, redirect, url_for, request,render_template
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

@app.route('/logout')
def logout():
	session.pop('username',None)
	return redirect('/')

if __name__ == '__main__':
   app.run(debug = True,host='0.0.0.0')
