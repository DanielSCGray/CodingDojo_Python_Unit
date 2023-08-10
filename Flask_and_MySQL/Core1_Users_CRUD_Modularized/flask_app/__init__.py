# __init__.py
from flask import Flask
app = Flask(__name__)

# if we use session we should have a secret key
# app.secret_key = "shhhhhh"
