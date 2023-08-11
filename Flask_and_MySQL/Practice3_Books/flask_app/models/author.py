from flask_app.config.mysql_connection import connect_to_mysql

DATABASE = 'books_schema'

class Author:
    def __init__(self, data):
        self.id = data['id']
        self.name = data['name']
        self.favorites = []

    @classmethod
    def create(cls, form_data):
        query = '''INSERT INTO authors (name)
        VALUE(%(name)s);
        '''
        author_id = connect_to_mysql(DATABASE).query_db(query, form_data)
        return author_id
    
    # @classmethod
    # def 