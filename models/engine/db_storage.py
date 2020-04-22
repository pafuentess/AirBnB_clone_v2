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
from sqlalchemy import create_engine, MetaData
from models.base_model import Base
import os


class DBStorage():
    """manager of mysql database"""
    __engine = None
    __session = None

    def __init__(self):

        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'.format(
                           os.environ.get("HBNB_MYSQL_USER"),
                           os.environ.get("HBNB_MYSQL_PWD"),
                           os.environ.get("HBNB_MYSQL_HOST"),
                           os.environ.get("HBNB_MYSQL_DB")),
                           pool_pre_ping=True)
        if (os.environ.get("HBNB_MYSQL_USER") == "test"):
            Base.metadata.drop_all(bind=self.__engine)

    def all(self, cls=None):
        """
        all
        """
        current = []
        objects = {}
        my_tables = {'cities': 'City', 'states': 'State', 'users': 'User',
                     'amenities': 'Amenity', 'places': 'Place',
                     'reviews': 'Review'}
        if cls:
            if type(cls) == str:
                current = self.__session.query(eval(cls)).all()
            else:
                current = self.__session.query(cls).all()
        else:
            tables = self.__engine.table_names()
            for table in tables:
                current.append(self.__session.query(
                    eval(my_tables[table])).all())
        for obj in current:
            if type(obj) == list:
                for o in obj:
                    key = "{}.{}".format(o.__class__.__name__, o.id)
                    objects[key] = o
            else:
                key = "{}.{}".format(obj.__class__.__name__, obj.id)
                objects[key] = obj
        return objects


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
        """ doc """
        if obj:
            self.__session.delete(obj)
            self.save()

    def reload(self):
        """serialize the file path to JSON file path
        """
        Base.metadata.create_all(bind=self.__engine)
        Session = scoped_session(sessionmaker(bind=self.__engine,
                                 expire_on_commit=False))
        self.__session = Session()

    def close(self):
        """ doc """
        self.__session.close()
