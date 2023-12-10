#!/usr/bin/python3
"""Test cases for file storage"""
import unittest
import os
import json
from unittest.mock import patch
from unittest.mock import mock_open
from models.base_model import BaseModel
from models import storage
from models.engine.file_storage import FileStorage


class TestFileStorage(unittest.TestCase):
    """Defines the test class for FileStorage testcases"""

    # For test_reload method
    read_data = {
        "BaseModel.1": {
            "__class__": "BaseModel",
            "id": "1",
            }
        }

    def setUp(self):
        """Reset the objects dictionary and
        reopen the file before each test
        """
        storage._FileStorage__objects = {}
        storage._FileStorage__file_path = "file.json"

    def tearDown(self):
        """Removes storage file at end of tests"""
        try:
            os.remove('file.json')
        except FileNotFoundError:
            pass

    # CLASS ATTRIBUTES TEST
    def test_objects_attribute_updated_on_new(self):
        """Test if __objects attribute
        is updated when a new object is added
        """
        obj = BaseModel()
        storage.new(obj)
        self.assertIn(f"BaseModel.{obj.id}", storage.all())

    # METHOD TESTS
    def test_all(self):
        """Test the all method, whether _objects is returned"""
        new_instance = BaseModel()
        new_instance.save()
        temp_dict = storage.all()
        self.assertIsInstance(temp_dict, dict)

    def test_new(self):
        """Test adding a new object to the objects dictionary"""
        obj = BaseModel()
        storage.new(obj)
        key = f"BaseModel.{obj.id}"
        self.assertIn(key, storage.all())
        self.assertEqual(storage.all()[key], obj)

    def test_save(self):
        """Test the save method, whether objects
        are correctly serialized to a JSON file
        """
        obj = BaseModel()
        storage.new(obj)
        storage.save()
        with open(storage._FileStorage__file_path, 'r') as data_file:
            data = json.load(data_file)
        self.assertEqual(data[f"BaseModel.{obj.id}"], obj.to_dict())

    @patch(
            "builtins.open", new_callable=mock_open,
            read_data=json.dumps(read_data)
            )
    def test_reload(self, mock_open_file):
        """Test the reload method, whether objects
        are correctly deserialized from a JSON file
        """
        storage.reload()
        obj = BaseModel()
        obj.id = "1"
        key = f"BaseModel.{obj.id}"
        self.assertEqual(storage.all()[key].id, obj.id)

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
        storage.reload()
        self.assertEqual(storage.all(), {})

    # OTHERS


if __name__ == '__main__':
    unittest.main()
