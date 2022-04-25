from db_utils import get_session

from models import Book
from faker import Faker

ssesion = get_session()
f = Faker()
for _ in range(30):
    title = f.word()
    author = f'{f.last_name()} {f.first_name()}'

    book = Book(title=title, author=author)
    ssesion.add(book)

ssesion.commit()