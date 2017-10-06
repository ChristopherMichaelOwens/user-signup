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
	
	
	if len(username) < 3 or len(username) > 20 or " " in username:
		error_user = "Please enter a username between 3 and 20 characters"
		

	if password!=verify or password == "":
		error_verify = "Passwords don't match"
		
		
	if len(password) < 3 or len(password) > 20 or " " in password:
		error_pass = "Please enter a password between 3 and 20 characters"
	
	if "@" not in email or "." not in email or " " in email:
		error_email = "You need a valid e-mail address."
	
	if len(email) < 3 or len(email) > 20 or " " in email:
		error_email = "Email needs to be between 3 and 20 characters"
	
	if email == "":
		error_email = ""
	
	if error_user != "" or error_pass != "" or error_verify != "" or error_email != "":
		return render_template('index.html', username = username, email = email,error_user = error_user, error_pass = error_pass, error_verify = error_verify, error_email = error_email)
		
		
	return render_template('welcome.html', username=username)
@app.route("/")
def index():
	return render_template('index.html', username = "", email = "")
app.run()