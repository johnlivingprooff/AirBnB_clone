#!/usr/bin/python3
"""Unittest for BaseModel"""
import unittest
from datetime import datetime
from models import storage
from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):
    """Test cases for the BaseModel Class"""

    def test_instance(self):
        """test instantisation"""
        obj = BaseModel()
        self.assertIsInstance(obj, BaseModel)
    
    def test_instance_hasattr(self):
        """Tests if an instance has attributes"""
        obj = BaseModel()

        self.assertTrue(hasattr(obj, 'id'))
        self.assertTrue(hasattr(obj, 'created_at'))
        self.assertTrue(hasattr(obj, 'updated_at'))

    def test_instance_with_value(self):
        """
        Test whether the instance attributes are correctly assigned
        """
        _id = "7q795"
        _created_at = "2023-12-07T09:49:07.936066"
        _updated_at = "2023-12-07T09:49:07.936176"
        d_format = "%Y-%m-%dT%H:%M:%S.%f"

        obj_c_at = datetime.strptime(_created_at, d_format)
        obj_u_at = datetime.strptime(_updated_at, d_format)
        obj = BaseModel(id=_id, created_at=_created_at, updated_at=_updated_at)

        self.assertEqual(obj.id, _id )
        self.assertEqual(obj.created_at, obj_c_at )
        self.assertEqual(obj.updated_at, obj_u_at )
        
    def test_str_method(self):
        """testing the __str__ method"""
        obj = BaseModel()
        expected_str = f"[BaseModel] ({obj.id}) {obj.__dict__}"
        self.assertEqual(str(obj), expected_str)

    def test_save_method(self):
        """test case for save method"""
        obj = BaseModel()
        first_update = obj.updated_at
        obj.user = "Testin"
        obj.save()
        self.assertNotEqual(first_update, obj.updated_at)

    def test_to_dict_method(self):
        """Test Case for to_dict method"""
        _id = "7q795"
        _created_at = "2023-12-07T09:49:07.936066"
        _updated_at = "2023-12-07T09:49:07.936176"

        obj = BaseModel(id=_id, created_at=_created_at, updated_at=_updated_at)
        obj_dict = obj.to_dict()
        dictionary = {'id': '7q795', 'created_at': "2023-12-07T09:49:07.936066", 'updated_at': "2023-12-07T09:49:07.936176", '__class__': "BaseModel"}
        self.assertEqual(dictionary, obj_dict)

    def test_inst_from_dict(self):
        pass

    def test_custom_datetime_format(self):
        pass

if __name__ == '__main__':
    unittest.main()
