from flask_app.config.mysql_connection import connect_to_mysql
from flask_app.models import message
import re
from flask import flash

# Set DATABASE below

DATABASE = 'private_wall_db'

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
NUMBERS_REGEX = re.compile(r'[0-9]')
UPPERCASE_REGEX = re.compile(r'[A-Z]')

class User:
    def __init__(self, data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']
        self.password = data['password']
        self.my_messages = []
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @staticmethod
    def validate_registration(data):
        is_valid = True
        if len(data['first_name'].strip()) < 2:
            is_valid = False 
            flash('First name must be 2+ characters')
        
        if len(data['last_name'].strip()) < 2:
            is_valid = False 
            flash('Last name must be 2+ characters')
        
        if len(data['email'].strip()) < 1:
            is_valid = False
            flash('Email not valid')
        elif not EMAIL_REGEX.match(data['email']):
            is_valid = False
            flash('Not a valid email')
        users = User.get_all()
        if is_valid:
            for obj in users:
                if data['email'] == obj.email:
                    is_valid = False
                    flash('An account with this email already exists')
                    break
        
        if len(data['password'].strip()) < 8:
            is_valid = False
            flash('Password must be at least 8 characters')
        elif not NUMBERS_REGEX.search(data['password']):
            is_valid = False
            flash('Password must include at least one number')
        elif not UPPERCASE_REGEX.search(data['password']):
            is_valid = False
            flash('Password must include at least uppercase letter')
        
        if not data['password'] == data['confirm_password']:
            is_valid = False
            flash('Password Confirmation must match')
        
        return is_valid



    @classmethod
    def create(cls, data):
        query = '''INSERT INTO users (first_name, last_name, email, password)
        VALUES (%(first_name)s, %(last_name)s, %(email)s, %(password)s);'''
        user_id = connect_to_mysql(DATABASE).query_db(query, data)
        return user_id
    
    @classmethod
    def get_all(cls):
        query = 'SELECT * FROM users;'
        result = connect_to_mysql(DATABASE).query_db(query)
        users = []
        for user in result:
            users.append(User(user))
        return users
    
    @classmethod 
    def get_by_email(cls, data):
        query = 'SELECT * FROM users WHERE email = %(email)s;'
        result = connect_to_mysql(DATABASE).query_db(query, data)
        if len(result) < 1:
            return False
        user = User(result[0])
        return user
    
    @classmethod
    def get_by_id(cls, user_id):
        query = '''
        select * from users 
        where id = %(user_id)s;
        '''
        data = {'user_id': user_id} 
        result = connect_to_mysql(DATABASE).query_db(query, data)
        user = User(result[0])
        return user

    @classmethod
    def get_with_messages(cls, user_id):
        query = '''SELECT * FROM users 
        LEFT JOIN messages ON messages.recipient_id = users.id
        WHERE users.id = %(user_id)s;'''
        data = {'user_id': user_id}
        results = connect_to_mysql(DATABASE).query_db(query, data)

        user = User(results[0])
        for row in results:
            if row['messages.id']:
                message_data = {
                    'id': row['messages.id'],
                    'content': row['content'],
                    'sender_id': row['sender_id'],
                    'recipient_id': row['recipient_id'],
                    'created_at' : row['messages.created_at'],
                    'updated_at' : row['messages.updated_at']
                }
                user.my_messages.append(message.Message(message_data))
        return user
    
    def recieved_mail_senders(self):
        iterable = []
        for message in self.my_messages:
            iterable.append(message.pair_message_and_sender())
        return iterable
