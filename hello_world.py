from flask import Flask, render_template

app=Flask(__name__)

@app.route('/')
def home():
	return('This is my first webpage')

@app.route('/mars')
def mars():
	return('This is Mars')

@app.route('/login')
def login():
	return('Please enter your login details')

@app.route('/contactdetails')
def contactdetails():
	return('Please enter your contact details')

app.run(debug=True)