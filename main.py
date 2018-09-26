from flask import Flask, request, redirect, render_template
import cgi 
import os
import re 


app = Flask(__name__, 
            static_url_path='', 
            static_folder='web/static',
            template_folder='web/templates')

app.config['DEBUG'] = True


@app.route('/', methods=['GET', 'POST'])
def display_signup_form():
    if request.method == 'GET':
        return render_template('index.html')

    username = request.form['username']
    pwd = request.form['pwd']
    pwd2 = request.form['pwd2']
    email = request.form['email']

    username_error = ''
    pwd_error = ''
    pwd2_error = ''
    email_error = ''

    ### Validation Conditionals: username ###
    if len(username) <3 or len(username) >20 or " " in username:   
        username_error = "InValid"


    ### Validation Conditionals: pwd ###
    if len(pwd) <3 or len(pwd) >20 or " " in pwd:
        pwd_error = "InValid"


    ### Validation Conditionals: pwd2 ###
    if pwd != pwd2:
        pwd2_error = "InValid"


    ### Validation Conditionals: email ###
    if email != '' and len(email) <3 or len(email) >20 and ("@" or "." not in email):    
        email_error = "InValid"
        email = ''
    

    ### Conditionals: welcome page ###
    if not username_error and not pwd_error and not pwd2_error and not email_error:
        return render_template('welcome.html', name=username)
    else:
        return render_template('index.html', username_error=username_error, 
        pwd_error=pwd_error, pwd2_error=pwd2_error, email_error=email_error, 
        username=username, pwd="", pwd2="", email=email)
   

    if not username_error and not pwd_error and not pwd2_error and not email_error:
        return render_template('welcome.html', name=username) 
    else:
        return render_template('index.html', username_error=username_error, 
        pwd_error=pwd_error, pwd2_error=pwd2_error, email_error=email_error, 
        username=username, pwd="", pwd2="", email=email)


app.run()

################# TODO Notes ################# 
# https://www.w3schools.com/tags/tag_input.asp
    #Bonus
    #regular expression to validate input fields 

