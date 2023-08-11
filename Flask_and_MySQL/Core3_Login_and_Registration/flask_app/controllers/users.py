from flask_app import app
from flask_app.models import user
from flask import redirect, render_template, request, session

@app.route('/')
def home():
    return render_template('index.html')

@app.post('/register')
def register():
    if not user.User.validate_registration(request.form):
        return redirect('/')
    return redirect('/welcome')

@app.post('/log_in')
def log_in():
    if not user.User.validate_login(request.form):
        return redirect('/')
    return redirect('/welcome')

@app.route('/welcome')
def welcome_page():
    return render_template('welcome.html')