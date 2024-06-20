## DON'T USE IPYNB FILE TYPE

from flask import Flask, redirect, url_for

app = Flask(__name__)

@app.route('/')
def hello():
    return 'Welcome to PC 18!'

if __name__ == '__main__':
    app.run(debug=True)