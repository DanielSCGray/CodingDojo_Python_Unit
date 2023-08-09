from users import User


from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)

@app.route('/')
def read_all():
    users = User.get_all()
    return render_template('read_all.html', users=users)

@app.post('/process')
def add_user():
    User.create(request.form)
    return redirect('/')

@app.route('/create')
def create():
    return render_template('create.html')


if __name__=="__main__":
    app.run(debug=True)