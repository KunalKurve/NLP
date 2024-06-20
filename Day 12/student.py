from flask import Flask, render_template, request
app = Flask(__name__)

@app.route('/')
def student():
    return render_template('readmarks.html')

@app.route('/result', methods =['GET', 'POST'])
def result():
    if request.method == 'POST':
        phys = int(request.form['phys'])
        chem = int(request.form['chem'])
        math = int(request.form['math'])

        avg = (phys + chem + math) / 3

        return (render_template('result.html', result=avg))

if __name__ == '__main__':
    app.run(debug=True)