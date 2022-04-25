import sqlite3

from flask import Flask, render_template
from utils import get_book
from db_utils import get_session
from models import Book

from variables import DEBUG, PORT, URL

app = Flask(__name__)


@app.route("/")
def index():
    return render_template('index.html')




@app.route('/books/list')
def list_books():
    s = get_session()
    books = s.query(Book).all()
    return render_template('books/list.html', books=books)



@app.route('/books/detail/<int:book_id>')
def detail_book(book_id):
    connection = get_db_connection()
    book = get_book(book_id,connection)
    return render_template('books/detail.html', book=book)


@app.route('/books/create', methods=['GET', 'POST'])
def create_book():
    if request.method == 'POST':
        title = request.form['title']
        author = request.form['author']

        if title and author:
            connection = get_db_connection()
            connection.execute('INSERT INTO books (title, author) VALUES (?, ?)', (title, author))
            connection.commit()
            connection.close()
            return redirect(url_for('list_books'))

    return render_template('books/create.html')


@app.route('/books/edit/<int:book_id>', methods=['GET', 'POST'])
def update_book(book_id):
    connection = get_db_connection()
    book = get_book(book_id, connection)

    if request.method == 'POST':
        title = request.form['title']
        author = request.form['author']

        if title and author:
            connection = get_db_connection()
            connection.execute('UPDATE books SET title = ?, author = ? WHERE id = ?', (title, author, book_id))
            connection.commit()
            connection.close()
            return redirect(url_for('list_books'))

    return render_template('books/edit.html', book=book)


@app.route('/books/delete/<int:book_id>', methods=('POST',))
def delete_book(book_id):
    if request.method == 'POST':
        connection = get_db_connection()
        connection.execute('DELETE FROM books WHERE id = ?', (book_id,))
        connection.commit()
        connection.close()

        return redirect(url_for('list_books'))


if __name__ == '__main__':
    app.run(debug=DEBUG, port=PORT)