#!/usr/bin/python
"""Unittests for DBStorage class of AirBnb_Clone_v2"""
import unittest
import pep8
import os
from os import getenv
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from models.engine.db_storage import DBStorage
from models.engine.file_storage import FileStorage
import MySQLdb
import models


@unittest.skipIf(
    os.getenv('HBNB_TYPE_STORAGE') != 'db',
    "This test only work in DBStorage")
class TestDBStorage(unittest.TestCase):
    '''this will test the DBStorage'''

    def teardown(cls):
        """at the end of the test this will tear it down"""
        self.session.close()
        sel.session.rollback()

    def test_pep8_DBStorage(self):
        """Tests pep8 style"""
        style = pep8.StyleGuide(quiet=True)
        p = style.check_files(['models/engine/db_storage.py'])
        self.assertEqual(p.total_errors, 0, "fix pep8")

    def test_all(self):
        """tests if all works in DB Storage"""
        storage = FileStorage()
        obj = storage.all()
        self.assertIsNotNone(obj)
        self.assertEqual(type(obj), dict)
        self.assertIs(obj, storage._FileStorage__objects)

    def test_new(self):
            """test when new is created"""
            storage = FileStorage()
            obj = storage.all()
            user = User()
            user.id = 123455
            user.name = "Kevin"
            storage.new(user)
            key = user.__class__.__name__ + "." + str(user.id)
            self.assertIsNotNone(obj[key])

    def test_reload_dbtorage(self):
            """
            tests reload
            """
            self.storage.save()
            Root = os.path.dirname(os.path.abspath("console.py"))
            path = os.path.join(Root, "file.json")
            with open(path, 'r') as f:
                lines = f.readlines()
            try:
                os.remove(path)
            except Exception:
                pass
            self.storage.save()
            with open(path, 'r') as f:
                lines2 = f.readlines()
            self.assertEqual(lines, lines2)
            try:
                os.remove(path)
            except Exception:
                pass
            with open(path, "w") as f:
                f.write("{}")
            with open(path, "r") as r:
                for line in r:
                    self.assertEqual(line, "{}")
            self.assertIs(self.storage.reload(), None)

    def _State(self):
        """doc"""
        state = State(name="Arizona")
        if state.id in models.storage.all():
            self.asserTrue(state.name, "Arizona")

    def _City(self):
        """doc"""
        city = City(name="medellin")
        if state.id in models.storage.all():
            self.asserTrue(city.name, "medellin")

    def _User(self):
        """doc"""
        user = User(name="paula", email="1@hal")
        if users.id in models.storage.all():
            self.asserTrue(user.name, "paula")
            self.asserTrue(user.email, "1@hal")

    def _Place(self):
        """doc"""
        place = Place(name="tintin", number_rooms=1, number_bathrooms=2)
        if place.id in models.storage.all():
            self.asserTrue(place.name, "tintin")
            self.asserTrue(place.number_rooms, "1")
            self.asserTrue(place.number_bathrooms, "2")

    def _Amenity(self):
        """doc"""
        amenity = Amenity(name="billar")
        if amenity.id in models.storage.all():
            self.asserTrue(amenity.name, "billar")

    def _Review(self):
        """doc"""
        review = Review(text="cool")
        if review.id in models.storage.all():
            self.asserTrue(review.text, "cool")


if __name__ == "__main__":
    unittest.main()
