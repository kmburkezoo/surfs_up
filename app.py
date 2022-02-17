from flask import Flask
app = Flask(__name__)
@app.route('/')
def hello_world():
    return 'Hello world'
# 
# def hello_name():
#     name = input('What is your name?')
#     return f'Hello, {name}!'