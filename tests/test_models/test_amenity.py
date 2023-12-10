#!/usr/bin/python3
"""Unittest for BaseModel"""
import unittest
from unittest.mock import patch
from datetime import datetime
from models import storage
from models.amenity import Amenity
from models.base_model import BaseModel


class TestAmenity(unittest.TestCase):
    """Test cases for Amenity class"""

    # BASIC TESTS
    def test_name(self):
        """checks for the class attribute: name"""
        amenity = Amenity()
        self.assertEqual(amenity.name, "")

    def test_instance_hasattr(self):
        """Tests if an Place instance has core attributes"""
        obj = Amenity()
        self.assertTrue(hasattr(obj, 'id'))
        self.assertTrue(hasattr(obj, 'created_at'))
        self.assertTrue(hasattr(obj, 'updated_at'))

    def test_BaseModel_subclass(self):
        """test if object is an instance of BaseModel"""
        obj = Amenity()
        self.assertIsInstance(obj, BaseModel)

    def test_class_instance(self):
        """test if object is an instance of BaseModel & Amenity"""
        obj = Amenity()
        self.assertIsInstance(obj, Amenity)

    def test_str_representation(self):
        """Test the __str__ method"""
        obj = Amenity(name='TestAmenity', id="7q")
        expected_str = f"[Amenity] ({obj.id}) {obj.__dict__}"
        self.assertEqual(str(obj), expected_str)

if __name__ == '__main__':
    unittest.main()
