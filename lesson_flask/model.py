from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine

from variables import URL

base = declarative_base()


class People(base):
    __tablename__ = 'customers'

    CustomerId = Column(Integer, primary_key=True, nullable=False)
    FirstName = Column(String(40), nullable=False)


engin = create_engine(URL)
base.metadata.create_all(engin)
