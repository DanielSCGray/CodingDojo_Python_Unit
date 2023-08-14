from flask_app.config.mysql_connection import connect_to_mysql
from flask_app.models import book


DATABASE = 'books_schema'

class Author:
    def __init__(self, data):
        self.id = data['id']
        self.name = data['name']
        self.favorite_books = []
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @classmethod
    def create(cls, form_data):
        query = '''INSERT INTO authors (name)
        VALUE(%(name)s);
        '''
        author_id = connect_to_mysql(DATABASE).query_db(query, form_data)
        return author_id
    
    @classmethod
    def get_all(cls):
        query = 'SELECT * FROM authors;'
        result = connect_to_mysql(DATABASE).query_db(query)
        authors = []
        for author in result:
            authors.append(Author(author))
        return authors
    
    @classmethod
    def get_author_with_favorites(cls, author_id):
        query = '''SELECT * FROM authors
        LEFT JOIN favorites ON favorites.author_id = authors.id
        LEFT JOIN books ON favorites.book_id = books.id
        WHERE authors.id = %(author_id)s;'''
        data = {'author_id': author_id}
        results = connect_to_mysql(DATABASE).query_db(query, data)

        author = Author(results[0])
        for row in results:
            book_data = {
                'id': row['books.id'],
                'title': row['title'],
                'page_count': row['page_count'],
                'created_at': row['books.created_at'],
                'updated_at': row['books.updated_at']
            }
            author.favorite_books.append(book.Book(book_data))
        return author
    
    @classmethod
    def add_favorite(cls, form_data):
        query = '''INSERT INTO favorites (author_id, book_id)
        VALUES (%(author_id)s, %(book_id)s);'''
        return connect_to_mysql(DATABASE).query_db(query, form_data)

