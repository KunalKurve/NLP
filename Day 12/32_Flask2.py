## DON'T USE IPYNB FILE TYPE

from flask import Flask, redirect, url_for

app = Flask(__name__)

@app.route('/admin')
def hello_admin():
    return 'Hello Admin!'

@app.route('/guest/<guest>')
def hello_guest(guest):
    return ('Hello %s is a Guest' %guest)

@app.route('/user/<name>')
def hello_user(name):
    if name.lower() == 'admin':
        return redirect(url_for("hello_admin"))
    else:
        return redirect(url_for('hello_guest', guest = name))

if __name__ == '__main__':
    app.run(debug=True)