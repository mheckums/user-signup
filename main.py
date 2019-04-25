from flask import Flask, request, redirect, render_template
import cgi

app = Flask(__name__)

app.config['DEBUG'] = True




@app.route('/', methods=['POST'])
def index():



@app.route('/login', methods=['GET'])
def login():
    


app.run()