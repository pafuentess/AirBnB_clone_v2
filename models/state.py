#!/usr/bin/python3
"""This is the state class"""
from models.base_model import BaseModel, Base
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from os import environ
from models.city import City
import models


class State(BaseModel, Base):
    """This is the class for State
    Attributes:
        name: input name
    """

#    __tablename__ = "states"

    if(environ.get("HBNB_TYPE_STORAGE") == "db"):
        __tablename__ = "states"
        name = Column(String(128), nullable=False)
        cities = relationship("City",  backref='state', cascade='delete')
    else:
        name = ""

        @property
        def cities(self):
            """ doc """

            city_list = []
            for city in models.storage.all("City").values():
                if city.state_id == self.id:
                    city_list.append(city)
            return city_list
