from flask_app import app
from flask_app.models import author
from flask_app.models import book
from flask import redirect, render_template, request

@app.route('/')
def home():
    authors = author.Author.get_all()
    return render_template('authors.html', authors=authors)
    

@app.route('/authors/<int:author_id>')
def show_author(author_id):
    this_author = author.Author.get_author_with_favorites(author_id)
    books = book.Book.get_all()
    return render_template('author_show.html', author = this_author, books = books)

    

@app.post('/process/author')
def new_author():
    author.Author.create(request.form)
    return redirect('/')
