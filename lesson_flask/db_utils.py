from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from variables import URL
from model import base


def get_session():
    engine = create_engine(URL)
    base.metadata.bind = engine
    db_session = sessionmaker(bind=engine)
    return db_session()