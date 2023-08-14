from flask_app.config.mysql_connection import connect_to_mysql
from flask_app.models import author


DATABASE = 'books_schema'

class Book:
    def __init__(self, data):
        self.id = data['id']
        self.title = data['title']
        self.page_count = data['page_count']
        self.favorited_authors = []
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @classmethod
    def create(cls, form_data):
        query = '''INSERT INTO books (title, page_count)
        VALUE(%(title)s, %(page_count)s);
        '''
        book_id = connect_to_mysql(DATABASE).query_db(query, form_data)
        return book_id
    
    @classmethod
    def get_all(cls):
        query = 'SELECT * FROM books;'
        result = connect_to_mysql(DATABASE).query_db(query)
        books = []
        for book in result:
            books.append(Book(book))
        return books
    
    @classmethod
    def get_book_with_favorites(cls, book_id):
        query = '''SELECT * FROM books
        LEFT JOIN favorites ON favorites.book_id = books.id
        LEFT JOIN authors ON favorites.author_id = authors.id
        WHERE books.id = %(book_id)s;'''
        data = {'book_id': book_id}
        results = connect_to_mysql(DATABASE).query_db(query, data)

        book = Book(results[0])
        for row in results:
            author_data = {
                'id': row['authors.id'],
                'name': row['name'],
                'created_at': row['authors.created_at'],
                'updated_at': row['authors.updated_at']
            }
            book.favorited_authors.append(author.Author(author_data))
        return book