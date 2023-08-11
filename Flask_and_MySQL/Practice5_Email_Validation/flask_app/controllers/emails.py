from flask_app import app
from flask_app.models import email
from flask import redirect, render_template, request, session

@app.route('/')
def home():
    return render_template('index.html')

@app.post('/process')
def validate():
    if not email.Email.validate_info(request.form):
        return redirect('/')
    email.Email.create(request.form)
    session['email'] = request.form['email']
    return redirect('/success')

@app.route('/success')
def show():
    emails = email.Email.get_all()
    return render_template('success.html', emails=emails)

@app.post('/delete')
def delete():
    email_id = request.form['email_id']
    email.Email.delete(email_id)
    return redirect('/success')
