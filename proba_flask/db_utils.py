import sqlite3
from variables import URL, URI_DB
from sqlalchemy.orm import sessionmaker
from sqlalchemy import  create_engine
from models import base

def get_db_connection():
    connection = sqlite3.connect(URL)
    connection.row_factory = sqlite3.Row
    return connection

def get_session():
    engine = create_engine(URI_DB)
    base.metadata.bind = engine
    db_session = sessionmaker(bind=engine)
    return db_session()

