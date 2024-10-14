import urllib.request
from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/yoto')
def yoto():
    yotoUrl = 'https://yoto.io/eb9jP?84jbYiDmy1gr=3qWnGm7RLt1CI' # crackling fire
    html = urllib.request.urlopen(yotoUrl)
    return html
