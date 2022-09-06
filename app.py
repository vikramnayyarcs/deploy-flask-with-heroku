from flask import Flask

app = Flask(__name__)


@app.route('/')
def index():
    return 'Hello World!'


@app.route('/about')
def about():
    return 'Deploy for fun.'
