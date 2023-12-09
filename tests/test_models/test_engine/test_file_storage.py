#!/usr/bin/python3
"""Test cases for file storage"""
import unittest
import os
from unittest.mock import patch
from unittest.mock import mock_open
from models.base_model import BaseModel
from models import storage


class TestFileStorage(unittest.TestCase):
    """Defines the test class for FileStorage testcases"""
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
        self.assertIn(key, storage._FileStorage__objects)
        self.assertEqual(storage._FileStorage__objects[key], obj)

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
        self.assertEqual(storage._FileStorage__objects, {})
