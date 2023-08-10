from flask_app import app
from flask_app.models.dojo import Dojo
from flask import redirect, render_template, request

@app.route('/dojos')
def home_page():
    dojos = Dojo.get_all()
    return render_template('dojos.html', dojos=dojos)

@app.post('/process/dojo')
def add_dojo():
    Dojo.create(request.form)
    return redirect('/dojos')

@app.route('/dojos/<int:dojo_id>')
def dojo_with_ninjas(dojo_id):
    dojo = Dojo.get_dojo_with_ninjas(dojo_id)
    return render_template('dojo_with_ninjas.html', dojo=dojo)