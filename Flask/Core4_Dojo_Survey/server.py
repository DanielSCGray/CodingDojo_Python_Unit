from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key = 'ea3fdb7f1bcf66419ab5eb540eecbc8dc82941cf7e073d49b4def6928d801f25'

@app.route('/')
def homepage():
    return render_template('index.html')

@app.route('/process', methods=['POST'])
def process():
    session['name'] = request.form['name']
    session['location'] = request.form['location']
    session['language'] = request.form['language']
    session['comments'] = request.form['comments']
    return redirect('/result')

@app.route('/result')
def result():

    return render_template('result.html')





if __name__=="__main__":
    app.run(debug=True)