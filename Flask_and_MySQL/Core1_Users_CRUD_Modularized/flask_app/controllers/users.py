from flask_app import app
from flask_app.models.user import User
from flask import redirect, render_template, request

@app.route('/')
def read_all():
    users = User.get_all()
    return render_template('read_all.html', users=users)

@app.post('/process')
def add_user():
    user_id = User.create(request.form)
    return redirect(f'/users/{user_id}')

@app.route('/create')
def create():
    return render_template('create.html')

@app.route('/users/<int:user_id>')
def show_user(user_id):
    user = User.get_one(user_id)
    return render_template('read_one.html', user=user)

@app.route('/users/<int:user_id>/edit')
def edit_user(user_id):
    user = User.get_one(user_id)
    return render_template('edit_user.html', user=user)

@app.post('/process/edit')
def update():
    User.update(request.form)
    user_id = request.form['user_id']
    return redirect(f'/users/{user_id}')

@app.route('/users/<int:user_id>/delete')
def delete_user(user_id):
    User.delete(user_id)
    return redirect('/')