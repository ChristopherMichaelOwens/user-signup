from flask import Flask, request, redirect, render_template
import cgi

app = Flask(__name__)

app.config['DEBUG'] = True

@app.route("/welcome", methods=['POST'])
def add_user():
	username = request.form['username']
	password = request.form['password']
	verify = request.form['verify']
	email = request.form['email']
	
	error_user = ""
	error_pass = ""
	error_verify = ""
	error_email = ""
	
	
	if len(username) < 3 or len(username) > 20 :
		error_user = "Please enter a username between 3 and 20 characters"
		

	if password!=verify:
		error_verify = "Passwords don't match"
		
		
	if len(password) < 3 or len(password) > 20:
		error_pass = "Please enter a password between 3 and 20 characters"
		
	
	if error_user or error_pass or error_verify:
		return render_template(username = username, email = email,error_user = error_user, error_pass = error_pass, error_verify = error_verify)
		
		
	return render_template('welcome.html', username=username)
@app.route("/")
def index():
	return render_template('index.html', username = "", email = "")
app.run()