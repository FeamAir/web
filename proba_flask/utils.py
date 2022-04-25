from werkzeug.exceptions import abort

def get_book(book_id,connection):
    book = connection.execute('SELECT * FROM books WHERE id = ?', (book_id,)).fetchone()
    connection.close()
    if book is None:
        abort(404)
    else:
        return book