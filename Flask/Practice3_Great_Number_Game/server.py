from random import random
from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key = 'ea3fdb7f1bcf66419ab5eb540eecbc8dc82941cf7e073d49b4def6928d801f25'

@app.route('/')
def home():
    if 'winning_number' not in session:
        session['winning_number'] = 
    return render_template('index.html')

if __name__=="__main__":
    app.run(debug=True)