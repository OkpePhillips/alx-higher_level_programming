#!/usr/bin/python3
"""
A python file that contains the class definition of a
State and an instance Base = declarative_base()
"""


from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String
from sqlalchemy import create_engine


Base = declarative_base()


class State(Base):
    """
    Class state that inherits from Base
    """

    __tablename__ = 'states'

    id = Column(Integer, primary_key=True, autoincrement=True,
                nullable=False)
    name = Column(String(128), nullable=False)


if __name__ == '__main__':
    from sqlalchemy import create_engine

    Base.metadata.create_all(engine)
