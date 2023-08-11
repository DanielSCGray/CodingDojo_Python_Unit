from flask_app.config.mysql_connection import connect_to_mysql
import re
from flask import flash

DATABASE = 'login_reg_db'

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

class User:
    def __init__(self, data):
        pass