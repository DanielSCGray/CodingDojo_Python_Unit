from flask_app import app
import json
from flask import jsonify, redirect, render_template, request, session, flash

@app.route('/')
def bar_page():
    return render_template('bar.html')