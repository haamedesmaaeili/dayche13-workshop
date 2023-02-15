from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, Dayche!'


@app.route('/bye')
def bye_dayche():
    return 'Bye, Dayche!'

@app.route('/hamed')
def bye_dayche():
    return 'Which Sandwich do you like?'
