from flask_app import app
from flask_app.models import student
from flask import render_template, redirect, request

@app.route('/')
def home():
    return render_template('index.html')

@app.post('/process')
def process_survey():
    if not student.Student.validate_info(request.form):
        return redirect('/')
    student.Student.create(request.form)
    return redirect('/result')

@app.route('/result')
def show_result():
    students = student.Student.get_all()
    return render_template('result.html', students=students)