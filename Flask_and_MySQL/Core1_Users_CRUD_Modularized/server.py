from flask_app.models.user import User
from flask_app.controllers import users

from flask_app import app
# from flask import Flask, render_template, request, redirect, session
# app = Flask(__name__)


if __name__=="__main__":
    app.run(debug=True)