from flask_app.config.mysql_connection import connect_to_mysql
from flask_app.models import user
from flask import flash

DATABASE = 'private_wall_db'

class Message:
    def __init__(self, data):
        self.id = data['id']
        #fill property in as needed, ctrl d 4 times to update create method aswell
        self.content = data['content']
        self.sender_id = data['sender_id']
        self.recipient_id = data['recipient_id']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @classmethod
    def create(cls, form_data):
        #delete excess props, remember parent/one in the relation's ID must be inserted by form aswell
        query = '''
        INSERT INTO messages (content, sender_id, recipient_id)
        VALUES (%(content)s, %(sender_id)s, %(recipient_id)s);
        '''
        message_id = connect_to_mysql(DATABASE).query_db(query, form_data)
        return message_id
    
    @classmethod
    def get_all(cls):
        query = 'SELECT * FROM messages;'
        result = connect_to_mysql(DATABASE).query_db(query)
        messages = []
        for message in result:
            messages.append(Message(message))
        return messages
    
    @classmethod
    def get_by_id(cls, message_id):
        query = 'SELECT * FROM messages WHERE id = %(message_id)s;'
        data = {'message_id': message_id}
        result = connect_to_mysql(DATABASE).query_db(query, data)
        message = Message(result[0])
        return message
    
    @classmethod
    def update(cls, form_data):
        #Remember the edit form should use a hidden input to provide the id of the message data being edited
        query = '''UPDATE messages
        SET content=%(content)s, sender_id=%(sender_id)s, recipient_id=%(recipient_id)s, property4=%(property4)s, property5=%(property5)s
        WHERE id = %(message_id)s;'''
        return connect_to_mysql(DATABASE).query_db(query, form_data)

    @classmethod
    def delete(cls, message_id):
        query = '''
        delete from messages where id = %(message_id)s;
        '''
        data = {'message_id': message_id}

        connect_to_mysql(DATABASE).query_db(query, data)
        return
    
    
    def get_sender(self):
        return user.User.get_by_id(self.sender_id)

    def pair_message_and_sender(self):
        return (self, self.get_sender())