from flask import Flask, redirect, url_for, request
app = Flask(__name__)

@app.route('/')
def index():
    return '''
            <html>
            <body>
            <h1>Hello User!</h1>
            @ CDAC Pune
            </body>
            </html>
'''


if __name__ == '__main__':
    app.run(debug=True)