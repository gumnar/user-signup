from flask import Flask, request, redirect, render_template
import cgi

app = Flask(__name__)

app.config['DEBUG'] #Displays runtime errors in the browser
def check_username():
    username = request.form['username']

    #Check length of username
    if len(username) < 3 or len(username) > 20:
        return False
    #Check for spaces in password
    for char in username:
        if char == ' ':
            return False
    return True

def check_password():
    password = request.form['password']

    #Check length of password
    if len(password) < 3 or len(password) > 20:
        return False
    #Check for spaces in password
    for char in password:
        if char == ' ':
            return False
    return True

def check_email():
    email = request.form['email']
    period_bool = False
    at_bool = False
    #If no email entered set to true
    if email == '' or email == " ":
        return True
    
    #Check email address
    for char in email.strip():
        #Verify no spaces
        if char == ' ':
            return False
        #Verify '.'
        if char == '.':
            period_bool = True
        #Verify @ symbol
        if char == '@':
            at_bool = True
    if period_bool == True and at_bool == True:
        return True
    #If no period or no @ then return False
    return False

def check_confirmpassword():
    password = request.form['password']
    confirmpassword = request.form['confirmpassword']

    if password == confirmpassword:
        return True
    return False

@app.route("/signup")
def sign_up():
    encoded_error = request.args.get('error')
    return render_template("signup.html")

@app.route("/welcome", methods=['POST'])
def welcome_message():
    username = request.form['username']

    #Init error reporting variables
    username_error = ''
    password_error = ''
    confirmpassword_error = ''
    email_error = ''

    if check_username() is False:
        username_error = "Invalid username"
    if check_password() is False:
        password_error = "Invalid password"
    if check_email() is False:
        email_error = "Invalid email address"
    if check_confirmpassword() is False:
        confirmpassword_error = "Passwords do not match"

    if check_username() and check_password() and check_confirmpassword() and check_email():
        return render_template("welcome.html", username = username)

    return redirect("/signup",
                            username_error = username_error,
                            password_error = password_error, 
                            email_error = email_error,
                            confirmpassword_error = confirmpassword_error)


#Route to the signup page until further notice
@app.route("/")
def index():
    
    return redirect('/signup')
    
app.run()