#!/usr/bin/python3
"""Unittest for User class"""
import unittest
import json
from unittest.mock import patch
from unittest.mock import mock_open
from unittest.mock import patch
from datetime import datetime
from models import storage
from models.user import User
from models.base_model import BaseModel


class TestUser(unittest.TestCase):
    """Test cases for User class"""

    # For test_reload method
    read_data = {
        "BaseModel.1": {
            "__class__": "BaseModel",
            "id": "1",
            }
        }

    # BASIC TESTS
    def test_email(self):
        """checks for class attribute email"""
        user = User()
        self.assertEqual(user.email, "")

    def test_instance_hasattr(self):
        """Tests if an user instance has core attributes"""
        obj = User()

        self.assertTrue(hasattr(obj, 'id'))
        self.assertTrue(hasattr(obj, 'created_at'))
        self.assertTrue(hasattr(obj, 'updated_at'))

    def test_BaseModel_subclass(self):
        """test if object is an instance of BaseModel"""
        obj = User()
        self.assertIsInstance(obj, BaseModel)

    def test_class_instance(self):
        """test if object is an instance of BaseModel & user"""
        obj = User()
        self.assertIsInstance(obj, User)

    def test_str_representation(self):
        """Test the __str__ method"""
        user = User(id="user-07")
        expected_str = f"[User] ({user.id}) {user.__dict__}"
        self.assertEqual(str(user), expected_str)

    def test_to_dict_method(self):
        """Test Case for to_dict method"""
        _id = "7q795"
        _created_at = "2023-12-07T09:49:07.936066"
        _updated_at = "2023-12-07T09:49:07.936176"
        _email = "youremail@mail.com"
        _password = "GHjhiu"
        _first_name = "First Name"
        _last_name = "Last Name"

        obj = User(
            id=_id, created_at=_created_at, updated_at=_updated_at,
            email=_email, password=_password, first_name=_first_name,
            last_name=_last_name)
        obj_dict = obj.to_dict()
        dictionary = {
            'id': '7q795', 'created_at': "2023-12-07T09:49:07.936066",
            'updated_at': "2023-12-07T09:49:07.936176",
            '__class__': "User", 'email': "youremail@mail.com",
            'password': "GHjhiu", 'first_name': "First Name",
            'last_name': "Last Name",
            }
        self.assertEqual(dictionary, obj_dict)

    def test_multiple_instances(self):
        """Test the behavior of multiple instances"""
        obj1 = User(email='email1@mail.com')
        obj2 = User(email='email2@mail.com')
        self.assertNotEqual(obj1, obj2)

    # ATTRIBUTES TESTS
    def test_with_args_id(self):
        """Test with specific args"""
        _id = "7q795"
        obj = User(id=_id)
        self.assertEqual(obj.id, _id)

    def test_with_args_created_at(self):
        """Test with specific created at time"""
        _created_at = "2023-12-07T09:49:07.936066"
        d_format = "%Y-%m-%dT%H:%M:%S.%f"
        obj_c_at = datetime.strptime(_created_at, d_format)
        obj = User(created_at=_created_at)
        self.assertEqual(obj.created_at, obj_c_at)

    def test_with_args_updated_at(self):
        """Test with specific updated at time"""
        _updated_at = "2023-12-07T09:49:07.936066"
        d_format = "%Y-%m-%dT%H:%M:%S.%f"
        obj_u_at = datetime.strptime(_updated_at, d_format)
        obj = User(created_at=_updated_at)
        self.assertEqual(obj.created_at, obj_u_at)

    def test_with_args_email(self):
        """Test with specific email"""
        _var = "youremail@mail.com"
        obj = User(email=_var)
        self.assertEqual(obj.email, _var)

    def test_with_args_password(self):
        """Test with specific password"""
        _var = "456gfg8*$#"
        obj = User(password=_var)
        self.assertEqual(obj.password, _var)

    def test_with_args_first_name(self):
        """Test with specific first name"""
        _var = "MyName"
        obj = User(first_name=_var)
        self.assertEqual(obj.first_name, _var)

    def test_with_args_first_name(self):
        """Test with specific last name"""
        _var = "surnName"
        obj = User(last_name=_var)
        self.assertEqual(obj.last_name, _var)

    def test_empty_email(self):
        """Test if the class handles empty email"""
        user = User(email='')
        self.assertEqual(user.email, '')

    def test_none_password(self):
        """Test if the class handles None password"""
        user = User(password=None)
        self.assertIsNone(user.password)

    def test_instance_has_class_attr(self):
        """Tests if an instance has class attributes"""
        obj = User()
        self.assertTrue(hasattr(obj, 'email'))
        self.assertTrue(hasattr(obj, 'password'))
        self.assertTrue(hasattr(obj, 'first_name'))
        self.assertTrue(hasattr(obj, 'last_name'))

    def test_same_details_unique_user(self):
        """Test if two instances with the same attributes are equal"""
        user1 = User(email='test@example.com', password='password')
        user2 = User(email='test@example.com', password='password')
        self.assertNotEqual(user1, user2)

    def test_inequality(self):
        """Test if two instances with different attributes are not equal"""
        user1 = User(email='test1@example.com', password='password1')
        user2 = User(email='test2@example.com', password='password2')
        self.assertNotEqual(user1, user2)

    # FileStorage Tests
    @patch('models.storage.save')
    def test_save_method_updates_storage(self, mock_save):
        """Test whether models.storage.save
        is called and updates the storage
        """
        user = User()
        original_updated_at = user.updated_at
        user.password = 'NewuserName'
        user.save()
        mock_save.assert_called_once()
        self.assertNotEqual(original_updated_at, user.updated_at)

    @patch('models.storage.new')  # helps to mock the new method
    def test_new_method_called_on_instance_creation(self, mock_new):
        """Test whether models.storage.new
        is called when creating an instance
        """
        obj = User()
        mock_new.assert_called_once_with(obj)

    @patch('models.storage.all')
    def test_all_method_returns_dict(self, mock_all):
        """Test whether models.storage.all returns a dictionary"""
        mock_all.return_value = {'some_key': 'some_value'}
        result = storage.all()
        self.assertIsInstance(result, dict)

    def test_empty_first_name(self):
        """Test if the class handles empty first_name"""
        user = User(first_name='')
        self.assertEqual(user.first_name, '')

    def test_none_last_name(self):
        """Test if the class handles None last_name"""
        user = User(last_name=None)
        self.assertIsNone(user.last_name)

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


if __name__ == '__main__':
    unittest.main()
