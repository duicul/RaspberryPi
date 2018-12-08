from flask import Flask,session,url_for, request
if 'username' in session:
    username = session['username']
    print(str(username))
else:
    print("anonymous")
