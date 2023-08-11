from flask_app.config.mysql_connection import connect_to_mysql
import re
from flask import flash

DATABASE = 'login_reg_db'

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

class User:
    def __init__(self, data):
        pass

    @staticmethod
    def validate_registration():
        pass

    @staticmethod
    def validate_login():
        pass

    @classmethod
    def create(cls, form_data):
        query = '''INSERT INTO users (first_name, last_name, email, password)
        VALUES ( %(first_name)s,  %(last_name)s, %(email)s, %(password)s,)'''
        pass