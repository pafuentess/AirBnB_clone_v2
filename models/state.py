#!/usr/bin/python3
"""This is the state class"""
from models.base_model import BaseModel, Base
from os import environ


class State(BaseModel, Base):
    """This is the class for State
    Attributes:
        name: input name
    """
    if(environ.get("HBNB_TYPE_STORAGE") == "db"):
        __tablename__ = "states"
        name = Column(String(128), nullable=False)
        cities = relationship("City",  backref='state', cascade='delete')
    elif(environ.get("HBNB_TYPE_STORAGE") == "file"):
        name = ""
        
