#!/usr/bin/python3
"""This is the state class"""
from models.base_model import BaseModel, Base
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from os import environ
from models.city import City


class State(BaseModel, Base):
    """This is the class for State
    Attributes:
        name: input name
    """

    __tablename__ = "states"

    if(environ.get("HBNB_TYPE_STORAGE") == "db"):
        name = Column(String(128), nullable=False)
        cities = relationship("City",  backref='state', cascade='delete')
    else:
        name = ""

        @property
        def cities(self):
            city = models.storage.all(City)
            relation = []
            for key in city.values():
                if key.states.id == self.id:
                    relation.append(key)
            return relation
