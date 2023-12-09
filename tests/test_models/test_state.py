#!/usr/bin/python3
"""Unittest for State class"""
import unittest
from unittest.mock import patch
from datetime import datetime
from models import storage
from models.state import State
from models.base_model import BaseModel


class TestState(unittest.TestCase):
    """Test cases for State class"""

    # BASIC TESTS
    def test_name(self):
        """checks for class attribute place_id"""
        state = State()
        self.assertEqual(state.name, "")

    def test_instance_hasattr(self):
        """Tests if an state instance has core attributes"""
        obj = State()

        self.assertTrue(hasattr(obj, 'id'))
        self.assertTrue(hasattr(obj, 'created_at'))
        self.assertTrue(hasattr(obj, 'updated_at'))

    def test_BaseModel_subclass(self):
        """test if object is an instance of BaseModel"""
        obj = State()
        self.assertIsInstance(obj, BaseModel)

    def test_class_instance(self):
        """test if object is an instance of BaseModel & state"""
        obj = State()
        self.assertIsInstance(obj, State)

    def test_str_representation(self):
        """Test the __str__ method"""
        state = State(name='TestState', id="7q")
        expected_str = f"[State] ({state.id}) {state.__dict__}"
        self.assertEqual(str(state), expected_str)

    def test_to_dict_method(self):
        """Test Case for to_dict method"""
        _id = "7q795"
        _created_at = "2023-12-07T09:49:07.936066"
        _updated_at = "2023-12-07T09:49:07.936176"
        _name = "the state"

        obj = State(
            id=_id, created_at=_created_at, updated_at=_updated_at,
            name=_name)
        obj_dict = obj.to_dict()
        dictionary = {
            'id': '7q795', 'created_at': "2023-12-07T09:49:07.936066",
            'updated_at': "2023-12-07T09:49:07.936176",
            '__class__': "State", 'name': "the state",
            }
        self.assertEqual(dictionary, obj_dict)

    def test_equality(self):
        """Test if two instances with the same attributes are equal"""
        state1 = State(name='California')
        state2 = State(name='California')
        self.assertEqual(state1.name, state2.name)

    def test_inequality(self):
        """Test if two instances with different attributes are not equal"""
        state1 = State(name='California')
        state2 = State(name='New York')
        self.assertNotEqual(state1, state2)

    def test_multiple_instances(self):
        """Test the behavior of multiple instances"""
        obj1 = State(name='State1')
        obj2 = State(name='State2')
        self.assertNotEqual(obj1, obj2)

    # ATTRIBUTES TESTS
    def test_with_args_id(self):
        """Test with specific args"""
        _id = "7q795"
        obj = State(id=_id)
        self.assertEqual(obj.id, _id)

    def test_with_args_created_at(self):
        """Test with specific created at time"""
        _created_at = "2023-12-07T09:49:07.936066"
        d_format = "%Y-%m-%dT%H:%M:%S.%f"
        obj_c_at = datetime.strptime(_created_at, d_format)
        obj = State(created_at=_created_at)
        self.assertEqual(obj.created_at, obj_c_at)

    def test_with_args_updated_at(self):
        """Test with specific updated at time"""
        _updated_at = "2023-12-07T09:49:07.936066"
        d_format = "%Y-%m-%dT%H:%M:%S.%f"
        obj_u_at = datetime.strptime(_updated_at, d_format)
        obj = State(created_at=_updated_at)
        self.assertEqual(obj.created_at, obj_u_at)

    def test_with_args_name(self):
        """Test with specific name"""
        _name = "TestState"
        obj = State(text=_name)
        self.assertEqual(obj.text, _name)

    def test_instance_has_class_attr(self):
        """Tests if an instance has class attributes"""
        obj = State()
        self.assertTrue(hasattr(obj, 'name'))

    def test_empty_name(self):
        """Test if the class handles empty name"""
        state = State(name='')
        self.assertEqual(state.name, '')

    def test_none_name(self):
        """Test if the class handles None created_at"""
        state = State(name=None)
        self.assertIsNone(state.name)

    # FileStorage Tests
    @patch('models.storage.save')
    def test_save_method_updates_storage(self, mock_save):
        """Test whether models.storage.save
        is called and updates the storage
        """
        state = State()
        original_updated_at = state.updated_at
        state.name = 'NewStateName'
        state.save()
        mock_save.assert_called_once()
        self.assertNotEqual(original_updated_at, state.updated_at)

    @patch('models.storage.new')  # helps to mock the new method
    def test_new_method_called_on_instance_creation(self, mock_new):
        """Test whether models.storage.new
        is called when creating an instance
        """
        obj = State()
        mock_new.assert_called_once_with(obj)

    @patch('models.storage.all')
    def test_all_method_returns_dict(self, mock_all):
        """Test whether models.storage.all returns a dictionary"""
        mock_all.return_value = {'some_key': 'some_value'}
        result = storage.all()
        self.assertIsInstance(result, dict)


if __name__ == '__main__':
    unittest.main()
