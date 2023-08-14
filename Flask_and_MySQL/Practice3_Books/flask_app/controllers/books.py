from flask_app import app
from flask_app.models import author
from flask_app.models import book
from flask import redirect, render_template, request

@app.route('/books')
def book_home():
    books = book.Book.get_all()
    return render_template('books.html', books=books)
    
@app.route('/books/<int:book_id>')
def show_book(book_id):
    this_book = book.Book.get_book_with_favorites(book_id)
    authors = author.Author.get_all()
    return render_template('book_show.html', book = this_book, authors = authors)

@app.post('/add_fav_b')
def add_favorite_b():
    author.Author.add_favorite(request.form)
    book_id = request.form['book_id']
    return redirect(f"/books/{book_id}")

@app.post('/process/book')
def add_book():
    book.Book.create(request.form)
    return redirect('/books')