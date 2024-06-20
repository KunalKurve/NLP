## DON'T USE IPYNB FILE TYPE

from flask import Flask

app = Flask(__name__)

@app.route('/<name>')
def hello_world(name):
    return ('Welcome %s' %name)

@app.route('/')
def hello():
    return 'This is home page'

@app.route('/welcome')
def welcome():
    return 'This is welcome page'

if __name__ == '__main__':
    app.run(debug=True)