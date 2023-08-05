import random
from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key = 'ea3fdb7f1bcf66419ab5eb540eecbc8dc82941cf7e073d49b4def6928d801f25'

@app.route('/')
def home():
    if 'winning_number' not in session:
        session['winning_number'] = random.randint(1, 100)
    return render_template('index.html')

@app.route('/guess', methods=['POST'])
def guess():
    session['user_guess'] = int(request.form['user_guess'])
    return redirect('/')

@app.route('/win', methods=['POST'])
def reset():
    session.clear()
    return redirect('/')

if __name__=="__main__":
    app.run(debug=True)