#!/usr/bin/python3
"""This is the file storage class for AirBnB"""
import json
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from sqlalchemy.orm import sessionmaker, scoped_session
from sqlalchemy import create_engine


class DBStorage():
    __engine = None
    __session = None

    def __init__(self):
        self.__engine = 'mysql+mysqldb://{}:{}@localhost/{}'.format(
                           environ.get("HBNB_MYSQL_USER"),
                           environ.get("HBNB_MYSQL_PWD"),
                           environ.get("HBNB_MYSQL_HOST"),
                           environ.get("HBNB_MYSQL_DB"),
                           pool_pre_ping=True)
        if (environ.get("HBNB_ENV") == "test"):
            Base.metadata.drop_all(bind=self.__engine)

    def all(self, cls=None):
        if cls:
            rows = self.__session.query("SELECT * FROM {}".format(cls))
        else:
            rows = self.__session.query("SELECT * FROM User, State, City, Amenity, Place, Review")

        lists = {}
        for key, item in rows.items():
            if item.__class__ == cls:
                lists[key] = item
        return lists

    def new(self, obj):
        """sets __object to given obj
        Args:
            obj: given object
        """
        self.__session.add(obj)
        self.save()

    def save(self):
        """serialize the file path to JSON file path
        """
        self.__session.commit()

    def delete(self, obj=None):
        if obj:
            self.__session.delete(obj)
            self.save()

    def reload(self):
        """serialize the file path to JSON file path
        """
        Base.metadata.create_all(self.__engine)
        self.__session = scoped_session(sessionmaker(bind=self.__engine, expire_on_commit=False))




