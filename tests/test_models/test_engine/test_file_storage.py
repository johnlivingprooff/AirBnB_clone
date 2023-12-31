#!/usr/bin/python3
"""Defines unittest for file storage"""
import os
import json
import models
import unittest
from datetime import datetime
from unittest.mock import patch
from unittest.mock import mock_open
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
from models.user import User
from models.state import State
from models.place import Place
from models.city import City
from models.amenity import Amenity
from models.review import Review


class TestFileStorage_instantiation(unittest.TestCase):
    """Unittests for testing instantiation of the FileStorage class."""

    def test_FileStorage_instantiation_no_args(self):
        """Test 1"""
        self.assertEqual(type(FileStorage()), FileStorage)

    def test_FileStorage_instantiation_with_arg(self):
        """Test 2"""
        with self.assertRaises(TypeError):
            FileStorage(None)

    def test_FileStorage_file_path_is_private_str(self):
        """Test 3"""
        self.assertEqual(str, type(FileStorage._FileStorage__file_path))

    def testFileStorage_objects_is_private_dict(self):
        """Test 4"""
        self.assertEqual(dict, type(FileStorage._FileStorage__objects))

    def test_storage_initializes(self):
        """Test 5"""
        self.assertEqual(type(models.storage), FileStorage)


class TestFileStorage_methods(unittest.TestCase):
    """Unittests for testing methods of the FileStorage class."""

    # For test_reload method
    read_data = {
        "BaseModel.1": {
            "__class__": "BaseModel",
            "id": "1",
            }
        }

    @classmethod
    def setUp(self):
        """Set Up Method"""
        try:
            os.rename("file.json", "tmp")
        except IOError:
            pass

    @classmethod
    def tearDown(self):
        """tearDown method"""
        try:
            os.remove("file.json")
        except IOError:
            pass
        try:
            os.rename("tmp", "file.json")
        except IOError:
            pass
        FileStorage._FileStorage__objects = {}

    def test_all(self):
        """Tests all"""
        self.assertEqual(dict, type(models.storage.all()))

    def test_all_with_arg(self):
        """Tests all with args"""
        with self.assertRaises(TypeError):
            models.storage.all(None)

    def test_new(self):
        """Test new"""
        base_m = BaseModel()
        user = User()
        state = State()
        place = Place()
        city = City()
        amenity = Amenity()
        review = Review()
        models.storage.new(base_m)
        models.storage.new(user)
        models.storage.new(state)
        models.storage.new(place)
        models.storage.new(city)
        models.storage.new(amenity)
        models.storage.new(review)
        self.assertIn("BaseModel." + base_m.id, models.storage.all().keys())
        self.assertIn(base_m, models.storage.all().values())
        self.assertIn("User." + user.id, models.storage.all().keys())
        self.assertIn(user, models.storage.all().values())
        self.assertIn("State." + state.id, models.storage.all().keys())
        self.assertIn(state, models.storage.all().values())
        self.assertIn("Place." + place.id, models.storage.all().keys())
        self.assertIn(place, models.storage.all().values())
        self.assertIn("City." + city.id, models.storage.all().keys())
        self.assertIn(city, models.storage.all().values())
        self.assertIn("Amenity." + amenity.id, models.storage.all().keys())
        self.assertIn(amenity, models.storage.all().values())
        self.assertIn("Review." + review.id, models.storage.all().keys())
        self.assertIn(review, models.storage.all().values())

    def test_new_with_args(self):
        """Tests new with args"""
        with self.assertRaises(TypeError):
            models.storage.new(BaseModel(), 1)

    def test_new_with_None(self):
        """Test new with none"""
        with self.assertRaises(AttributeError):
            models.storage.new(None)

    def test_save(self):
        """Test Save"""
        base_m = BaseModel()
        user = User()
        state = State()
        place = Place()
        city = City()
        amenity = Amenity()
        review = Review()
        models.storage.new(base_m)
        models.storage.new(user)
        models.storage.new(state)
        models.storage.new(place)
        models.storage.new(city)
        models.storage.new(amenity)
        models.storage.new(review)
        models.storage.save()
        save_text = ""
        with open("file.json", "r") as f:
            save_text = f.read()
            self.assertIn("BaseModel." + base_m.id, save_text)
            self.assertIn("User." + user.id, save_text)
            self.assertIn("State." + state.id, save_text)
            self.assertIn("Place." + place.id, save_text)
            self.assertIn("City." + city.id, save_text)
            self.assertIn("Amenity." + amenity.id, save_text)
            self.assertIn("Review." + review.id, save_text)

    def test_save_with_arg(self):
        """Tests save with args"""
        with self.assertRaises(TypeError):
            models.storage.save(None)

    def test_reload(self):
        """Tests Reload"""
        base_m = BaseModel()
        user = User()
        state = State()
        place = Place()
        city = City()
        amenity = Amenity()
        review = Review()
        models.storage.new(base_m)
        models.storage.new(user)
        models.storage.new(state)
        models.storage.new(place)
        models.storage.new(city)
        models.storage.new(amenity)
        models.storage.new(review)
        models.storage.save()
        models.storage.reload()
        objs = FileStorage._FileStorage__objects
        self.assertIn("BaseModel." + base_m.id, objs)
        self.assertIn("User." + user.id, objs)
        self.assertIn("State." + state.id, objs)
        self.assertIn("Place." + place.id, objs)
        self.assertIn("City." + city.id, objs)
        self.assertIn("Amenity." + amenity.id, objs)
        self.assertIn("Review." + review.id, objs)

    def test_reload_with_arg(self):
        """Tests Reload with args"""
        with self.assertRaises(TypeError):
            models.storage.reload(None)

    # FILE STORAGE TESTS
    @patch('models.storage.save')  # helpst to mock save method
    def test_save_method_updates_storage(self, mock_save):
        """Test whether models.storage.save
        is called and updates the storage
        """
        obj = BaseModel()
        original_updated_at = obj.updated_at

        # Modify some attributes to trigger the need to save
        obj.some_attribute = 'new_value'

        obj.save()
        mock_save.assert_called_once()

        # Verify that updated_at has changed after saving
        self.assertNotEqual(original_updated_at, obj.updated_at)

    @patch('models.storage.new')  # helps to mock the new method
    def test_new_method_called_on_instance_creation(self, mock_new):
        """Test whether models.storage.new
        is called when creating an instance
        """
        obj = BaseModel()
        mock_new.assert_called_once_with(obj)

    @patch("builtins.open", new_callable=mock_open, read_data='{}')
    def test_reload_no_file(self, mock_open_file):
        # Test reloading when the file doesn't exist
        models.storage.reload()
        self.assertEqual(models.storage.all(), {})

    @patch(
            "builtins.open", new_callable=mock_open,
            read_data=json.dumps(read_data)
            )
    def test_reload(self, mock_open_file):
        """Test the reload method, whether objects
        are correctly deserialized from a JSON file
        """
        models.storage.reload()
        obj = BaseModel()
        obj.id = "1"
        key = f"BaseModel.{obj.id}"
        self.assertEqual(models.storage.all()[key].id, obj.id)


if __name__ == "__main__":
    unittest.main()
