import os
from flask import Flask
from flask import request

app = Flask(__name__)

@app.route('/hello_world')
def hello_world():
    return "OK from inside the sp!"

if __name__ == '__main__':
    app.run(host='0.0.0.0')
