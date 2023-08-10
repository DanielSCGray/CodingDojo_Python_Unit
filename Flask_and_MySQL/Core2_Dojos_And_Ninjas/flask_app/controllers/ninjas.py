from flask_app import app
from flask_app.models.dojo import Dojo
from flask_app.models.ninja import Ninja
from flask import redirect, render_template, request

@app.route('/add_ninja')
def add_ninja():
    dojos = Dojo.get_all()
    return render_template('add_ninja.html', dojos=dojos)

@app.post('/process/ninja')
def process_new_ninja():
    Ninja.create(request.form)
    return redirect('/dojos')