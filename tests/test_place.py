#!/usr/bin/python3
"""Unittest for Place class"""
import unittest
from unittest.mock import patch
from datetime import datetime
from models import storage
from models.place import Place
from models.base_model import BaseModel


class Testplace(unittest.TestCase):
    """Test cases for place class"""

    # BASIC TESTS
    def test_city_id(self):
        """checks for class attribute state_id"""
        place = Place()
        self.assertEqual(place.city_id, "")

    def test_name(self):
        """checks for name class attribute"""
        place = Place()
        self.assertEqual(place.name, "")

    def test_user_id(self):
        """checks for user id class attribute"""
        place = Place()
        self.assertEqual(place.user_id, "")

    def test_description(self):
        """checks for description class attribute"""
        place = Place()
        self.assertEqual(place.description, "")

    def test_number_rooms(self):
        """checks for number rooms clase attribute"""
        place = Place()
        self.assertEqual(place.number_rooms, 0)

    def test_number_bathrooms(self):
        """checks for number of bathrooms clase attribute"""
        place = Place()
        self.assertEqual(place.number_bathrooms, 0)

    def test_max_guest(self):
        """checks for max guest clase attribute"""
        place = Place()
        self.assertEqual(place.max_guest, 0)

    def test_price_by_night(self):
        """checks for price/night clase attribute"""
        place = Place()
        self.assertEqual(place.price_by_night, 0)

    def test_latitude(self):
        """checks for latitude clase attribute"""
        place = Place()
        self.assertEqual(place.latitude, 0.0)

    def test_longitude(self):
        """checks for longitude clase attribute"""
        place = Place()
        self.assertEqual(place.longitude, 0.0)

    def test_amenity_ids(self):
        """checks for amenity id clase attribute"""
        place = Place()
        self.assertEqual(place.amenity_ids, [])

    def test_instance_hasattr(self):
        """Tests if an Place instance has core attributes"""
        obj = Place()

        self.assertTrue(hasattr(obj, 'id'))
        self.assertTrue(hasattr(obj, 'created_at'))
        self.assertTrue(hasattr(obj, 'updated_at'))

    def test_BaseModel_subclass(self):
        """test if object is an instance of BaseModel"""
        obj = Place()
        self.assertIsInstance(obj, BaseModel)

    def test_class_instance(self):
        """test if object is an instance of BaseModel & place"""
        obj = Place()
        self.assertIsInstance(obj, Place)

    def test_str_representation(self):
        """Test the __str__ method"""
        place = Place(name='Testplace', id="7q")
        expected_str = f"[Place] ({place.id}) {place.__dict__}"
        self.assertEqual(str(place), expected_str)

    def test_to_dict_method(self):
        """Test Case for to_dict method"""
        _id = "7q795"
        _created_at = "2023-12-07T09:49:07.936066"
        _updated_at = "2023-12-07T09:49:07.936176"
        _name = "the place"
        _city_id = "testCity"
        _user_id = _id
        _description = "place desc"
        _number_rooms = 0
        _number_bathrooms = 0
        _max_guest = 0
        _price_by_night = 0
        _latitude = 0.0
        _longitude = 0.0
        _amenity_ids = []

        obj = Place(
            id=_id, created_at=_created_at, updated_at=_updated_at,
            city_id=_city_id, amenity_ids=_amenity_ids,
            name=_name, user_id=_user_id, description=_description,
            number_rooms=_number_rooms, number_bathrooms=_number_bathrooms,
            max_guest=_max_guest, price_by_night=_price_by_night,
            latitude=_latitude, longitude=_longitude
            )
        obj_dict = obj.to_dict()
        dictionary = {
            'id': '7q795', 'created_at': "2023-12-07T09:49:07.936066",
            'updated_at': "2023-12-07T09:49:07.936176",
            '__class__': "Place", 'name': "the place",
            'city_id': "testCity", 'user_id': '7q795',
            'description': "place desc", 'number_rooms': 0,
            'number_bathrooms': 0, 'max_guest': 0, 'price_by_night': 0,
            'latitude': 0.0, 'longitude': 0.0, 'amenity_ids': [],
            }
        self.assertEqual(dictionary, obj_dict)

    def test_multiple_instances(self):
        """Test the behavior of multiple instances"""
        obj1 = Place(city_id='City1')
        obj2 = Place(city_id='City2')
        self.assertNotEqual(obj1, obj2)

    # ATTRIBUTES TESTS
    def test_with_args_id(self):
        """Test with specific args"""
        _id = "7q795"
        obj = Place(id=_id)
        self.assertEqual(obj.id, _id)

    def test_with_args_created_at(self):
        """Test with specific created at time"""
        _created_at = "2023-12-07T09:49:07.936066"
        d_format = "%Y-%m-%dT%H:%M:%S.%f"
        obj_c_at = datetime.strptime(_created_at, d_format)
        obj = Place(created_at=_created_at)
        self.assertEqual(obj.created_at, obj_c_at)

    def test_with_args_updated_at(self):
        """Test with specific updated at time"""
        _updated_at = "2023-12-07T09:49:07.936066"
        d_format = "%Y-%m-%dT%H:%M:%S.%f"
        obj_u_at = datetime.strptime(_updated_at, d_format)
        obj = Place(created_at=_updated_at)
        self.assertEqual(obj.created_at, obj_u_at)

    def test_with_args_city_id(self):
        """Test with specific state id"""
        _city_id = "oldState"
        obj = Place(state_id=_city_id)
        self.assertEqual(obj.state_id, _city_id)

    def test_with_args_name(self):
        """Test with specific name"""
        _name = "Testplace"
        obj = Place(name=_name)
        self.assertEqual(obj.name, _name)

    def test_instance_has_class_attr(self):
        """Tests if an instance has class attributes"""
        obj = Place()
        self.assertTrue(hasattr(obj, 'city_id'))
        self.assertTrue(hasattr(obj, 'user_id'))
        self.assertTrue(hasattr(obj, 'name'))
        self.assertTrue(hasattr(obj, 'description'))
        self.assertTrue(hasattr(obj, 'number_rooms'))
        self.assertTrue(hasattr(obj, 'number_bathrooms'))
        self.assertTrue(hasattr(obj, 'max_guest'))
        self.assertTrue(hasattr(obj, 'price_by_night'))
        self.assertTrue(hasattr(obj, 'latitude'))
        self.assertTrue(hasattr(obj, 'longitude'))
        self.assertTrue(hasattr(obj, 'amenity_ids'))

    # FileStorage Tests
    @patch('models.storage.save')
    def test_save_method_updates_storage(self, mock_save):
        """Test whether models.storage.save
        is called and updates the storage
        """
        place = Place()
        original_updated_at = place.updated_at
        place.name = 'NewplaceName'
        place.save()
        mock_save.assert_called_once()
        self.assertNotEqual(original_updated_at, place.updated_at)

    @patch('models.storage.new')  # helps to mock the new method
    def test_new_method_called_on_instance_creation(self, mock_new):
        """Test whether models.storage.new
        is called when creating an instance
        """
        obj = Place()
        mock_new.assert_called_once_with(obj)

    @patch('models.storage.all')
    def test_all_method_returns_dict(self, mock_all):
        """Test whether models.storage.all returns a dictionary"""
        mock_all.return_value = {'some_key': 'some_value'}
        result = storage.all()
        self.assertIsInstance(result, dict)


if __name__ == '__main__':
    unittest.main()
