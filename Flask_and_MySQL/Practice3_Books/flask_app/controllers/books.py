from flask_app import app
from flask_app.models import author
from flask_app.models import book
from flask import redirect, render_template, request

@app.route('/books')
def book_home():
    pass