from flask_app import app
from flask_app.models import user
from flask import redirect, render_template, request, session, flash
from flask_bcrypt import Bcrypt

bcrypt = Bcrypt(app)

@app.route('/')
def home():
    return render_template('index.html')

@app.post('/register')
def register():
    if not user.User.validate_registration(request.form):
        return redirect('/')
    password_hash = bcrypt.generate_password_hash(request.form['password'])
    data = {
        'first_name': request.form['first_name'],
        'last_name': request.form['last_name'],
        'email': request.form['email'],
        'password': password_hash
    }
    user_id = user.User.create(data)
    session['user_id'] = user_id
    return redirect('/welcome')

@app.post('/log_in')
def log_in():
    data = { 'email': request.form['email'] }
    current_user = user.User.get_by_email(data)
    if not current_user:
        flash('Invalid email/password')
        return redirect('/')
    if not bcrypt.check_password_hash(current_user.password, request.form['password']):
        flash('Invalid email/password')
        return redirect('/')
    session['user_id'] = current_user.id
    return redirect('/welcome')



@app.post('/log_out')
def log_out():
    session.clear()
    return redirect('/')
