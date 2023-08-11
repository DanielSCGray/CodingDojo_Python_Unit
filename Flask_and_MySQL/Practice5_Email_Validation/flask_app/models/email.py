from flask_app.config.mysql_connection import connect_to_mysql
import re
from flask import flash

DATABASE = 'email_db'

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

class Email:
    def __init__(self, data):
        self.id = data['id']
        self.email = data['email']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @staticmethod
    def validate_info(data):
        is_valid = True
        if len(data['email'].strip()) < 1:
            is_valid = False
            flash('Email not valid')
        elif not EMAIL_REGEX.match(data['email']):
            is_valid = False
            flash('Not a valid email')
        
        emails = Email.get_all()

        if is_valid:
            for obj in emails:
                if data['email'] == obj.email:
                    is_valid = False
                    flash('Email is valid, but already in the database.')
                    break
        

        return is_valid

    @classmethod
    def create(cls, form_data):
        query = '''INSERT INTO emails (email)
        VALUES (%(email)s);'''
        email_id = connect_to_mysql(DATABASE).query_db(query, form_data)
        return email_id
    
    @classmethod
    def get_all(cls):
        query = 'SELECT * FROM emails;'
        result = connect_to_mysql(DATABASE).query_db(query)
        emails = []
        for email in result:
            emails.append(Email(email))
        return emails
    
    @classmethod
    def delete(cls, email_id):
        query = 'DELETE FROM emails WHERE id = %(email_id)s;'
        data = {'email_id': email_id}
        connect_to_mysql(DATABASE).query_db(query, data)
        return

