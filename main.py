from flask import Flask, request, redirect, render_template, url_for
import cgi

app = Flask(__name__)

app.config['DEBUG'] = True 

@app.route("/")
def display_form():
    return render_template('index.html')

@app.route("/", methods=['POST'])
def index():
    user_password = request.form['user_password']
    confirmed_password = request.form['confirmed_password']
    username = request.form['username'] 
    email = request.form['email']

    username_error = ""
    username_length_error = ""
    empty_password_error = ""
    password_error = ""
    invalid_email_error = ""
    

    
    if ' ' in username or username == '' or len(username) < 3 or len(username) > 20:
        username_error = "Username must contain between 3-20 charcters and may not contain any spaces."

   
        
    if ' ' in user_password or len(user_password) < 3 or len(user_password) > 20 or user_password != confirmed_password or user_password == "" or confirmed_password == "":
        password_error = "Passwords must match and cannot be left blank."

    if email != "":
        if ' ' in email or "." not in email or "@" not in email or len(email) < 3 or len(email) > 20:
            
            invalid_email_error = "Please enter a valid E-mail address."
       
        email_list = email.split('@')
        at_count = len(email_list)
        period_email_list = email.split('.')  
        period_count = len(period_email_list)  
        if at_count > 2 or period_count > 2:
            invalid_email_error = "Please enter a valid E-mail address."



    if not username_error and not empty_password_error and not password_error and not invalid_email_error:
        return redirect("/welcome?username=" + username)
    


    else:
        return render_template('index.html', username=username, 
        username_error=username_error,
        user_password=user_password,
        confirmed_password=confirmed_password,
        empty_password_error=empty_password_error,
        password_error=password_error,
        invalid_email_error=invalid_email_error,
        email=email)



@app.route("/welcome")
def welcome():
    username = request.args.get('username')
    return render_template('welcome.html', username=username)


app.run()

