#!/usr/bin/python3
"""Unittest for Review class"""
import unittest
from unittest.mock import patch
from datetime import datetime
from models import storage
from models.review import Review
from models.base_model import BaseModel


class TestReview(unittest.TestCase):
    """Test cases for Review class"""

    # BASIC TESTS
    def test_place_id(self):
        """checks for class attribute place_id"""
        review = Review()
        self.assertEqual(review.place_id, "")

    def test_text(self):
        """checks for text class attribute"""
        review = Review()
        self.assertEqual(review.text, "")

    def test_user_id(self):
        """checks for user id class attribute"""
        review = Review()
        self.assertEqual(review.user_id, "")

    def test_instance_hasattr(self):
        """Tests if an review instance has core attributes"""
        obj = Review()

        self.assertTrue(hasattr(obj, 'id'))
        self.assertTrue(hasattr(obj, 'created_at'))
        self.assertTrue(hasattr(obj, 'updated_at'))

    def test_BaseModel_subclass(self):
        """test if object is an instance of BaseModel"""
        obj = Review()
        self.assertIsInstance(obj, BaseModel)

    def test_class_instance(self):
        """test if object is an instance of BaseModel & review"""
        obj = Review()
        self.assertIsInstance(obj, Review)

    def test_str_representation(self):
        """Test the __str__ method"""
        review = Review(name='TestReview', id="7q")
        expected_str = f"[Review] ({review.id}) {review.__dict__}"
        self.assertEqual(str(review), expected_str)

    def test_to_dict_method(self):
        """Test Case for to_dict method"""
        _id = "7q795"
        _created_at = "2023-12-07T09:49:07.936066"
        _updated_at = "2023-12-07T09:49:07.936176"
        _text = "the review"
        _place_id = "testCity"
        _user_id = _id

        obj = Review(
            id=_id, created_at=_created_at, updated_at=_updated_at,
            place_id=_place_id, text=_text, user_id=_user_id)
        obj_dict = obj.to_dict()
        dictionary = {
            'id': '7q795', 'created_at': "2023-12-07T09:49:07.936066",
            'updated_at': "2023-12-07T09:49:07.936176",
            '__class__': "Review", 'text': "the review",
            'place_id': "testCity", 'user_id': '7q795',
            }
        self.assertEqual(dictionary, obj_dict)

    def test_multiple_instances(self):
        """Test the behavior of multiple instances"""
        obj1 = Review(user_id='User1')
        obj2 = Review(user_id='User2')
        self.assertNotEqual(obj1, obj2)

    # ATTRIBUTES TESTS
    def test_with_args_id(self):
        """Test with specific args"""
        _id = "7q795"
        obj = Review(id=_id)
        self.assertEqual(obj.id, _id)

    def test_with_args_created_at(self):
        """Test with specific created at time"""
        _created_at = "2023-12-07T09:49:07.936066"
        d_format = "%Y-%m-%dT%H:%M:%S.%f"
        obj_c_at = datetime.strptime(_created_at, d_format)
        obj = Review(created_at=_created_at)
        self.assertEqual(obj.created_at, obj_c_at)

    def test_with_args_updated_at(self):
        """Test with specific updated at time"""
        _updated_at = "2023-12-07T09:49:07.936066"
        d_format = "%Y-%m-%dT%H:%M:%S.%f"
        obj_u_at = datetime.strptime(_updated_at, d_format)
        obj = Review(created_at=_updated_at)
        self.assertEqual(obj.created_at, obj_u_at)

    def test_with_args_place_id(self):
        """Test with specific state id"""
        _place_id = "oldState"
        obj = Review(place_id=_place_id)
        self.assertEqual(obj.place_id, _place_id)

    def test_with_args_text(self):
        """Test with specific name"""
        _name = "Testreview"
        obj = Review(text=_name)
        self.assertEqual(obj.text, _name)

    def test_instance_has_class_attr(self):
        """Tests if an instance has class attributes"""
        obj = Review()
        self.assertTrue(hasattr(obj, 'place_id'))
        self.assertTrue(hasattr(obj, 'user_id'))
        self.assertTrue(hasattr(obj, 'text'))

    # FileStorage Tests
    @patch('models.storage.save')
    def test_save_method_updates_storage(self, mock_save):
        """Test whether models.storage.save
        is called and updates the storage
        """
        review = Review()
        original_updated_at = review.updated_at
        review.name = 'NewReviewName'
        review.save()
        mock_save.assert_called_once()
        self.assertNotEqual(original_updated_at, review.updated_at)

    @patch('models.storage.new')  # helps to mock the new method
    def test_new_method_called_on_instance_creation(self, mock_new):
        """Test whether models.storage.new
        is called when creating an instance
        """
        obj = Review()
        mock_new.assert_called_once_with(obj)

    @patch('models.storage.all')
    def test_all_method_returns_dict(self, mock_all):
        """Test whether models.storage.all returns a dictionary"""
        mock_all.return_value = {'some_key': 'some_value'}
        result = storage.all()
        self.assertIsInstance(result, dict)


if __name__ == '__main__':
    unittest.main()
