from flask import Flask, request  

app = Flask(__name__)



@app.route('/')   #here it's just creating a route for root
def home_page():
    return "Here is the home page"

@app.route('/welcome')
def welcome():
     return "Here is the welcome page"

@app.route('/welcome/home')
def welcome_home():
     return "Welcome home"

@app.route('/welcome/back')
def welcome_back():
     return "Welcome back"