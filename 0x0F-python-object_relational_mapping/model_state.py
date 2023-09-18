#!/usr/bin/python3
"""
A python file that contains the class definition of a
State and an instance Base = declarative_base()
"""


from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String
from sqlalchemy import create_engine
import sys
from sqlalchemy.orm import relationship
from model_city import City


Base = declarative_base()


class State(Base):
    """
    Class state that inherits from Base
    """

    __tablename__ = 'states'

    id = Column(Integer, primary_key=True, autoincrement=True,
                nullable=False)
    name = Column(String(128), nullable=False)
    cities = relationship("City", back_populates="state")


engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
                       sys.argv[1], sys.argv[2], sys.argv[3]))

if __name__ == '__main__':
    Base.metadata.create_all(engine)
