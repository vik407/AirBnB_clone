#!/usr/bin/python3
"""BaseModel test file
"""

import unittest
import os
import pep8
# import models
from models.base_model import BaseModel
from models.amenity import Amenity


class TestAmenity(unittest.TestCase):
    """Set the test for base model class
    """
    
    # First things first, the setupclass
    @classmethod
    def setUpClass(cls):
        """Called before test in an individual class are run
        """
        cls.a = Amenity()
        cls.a.name = "Pool"

    @classmethod
    def tearDown(cls):
        """Called after test in an individual class have run
        """
        del cls.a

    # Clean after run tests
    def tearDown(self):
        """Clean file created after run the test (json file)
        """
        try:
            os.remove("file.json")
        except FileNotFoundError:
            pass

    # Run pep8 validate amenity.py
    def test_amenity_py(self):
        """pep8 amenity.py test
        """
        s = pep8.StyleGuide(quiet=True)
        f = s.check_files(['models/amenity.py'])
        self.assertEqual(f.total_errors, 0, 'pep8 error found!')

    def test_pep8_Amenity(self):
        """Tests pep8 style"""
        style = pep8.StyleGuide(quiet=True)
        p = style.check_files(['models/amenity.py'])
        self.assertEqual(p.total_errors, 0, "fix pep8")

    def test_checking_for_docstring_Amenity(self):
        """checking for docstrings"""
        self.assertIsNotNone(Amenity.__doc__)

    def test_attributes_Amenity(self):
        """chekcing if amenity have attibutes"""
        self.assertTrue('id' in self.a.__dict__)
        self.assertTrue('created_at' in self.a.__dict__)
        self.assertTrue('updated_at' in self.a.__dict__)
        self.assertTrue('name' in self.a.__dict__)

    def test_is_subclass_Amenity(self):
        """test if Amenity is subclass of Basemodel"""
        self.assertTrue(issubclass(self.a.__class__, BaseModel), True)

    def test_attribute_types_Amenity(self):
        """test attribute type for Amenity"""
        self.assertEqual(type(self.a.name), str)

    def test_save_Amenity(self):
        """test if the save works"""
        self.a.save()
        self.assertNotEqual(self.a.created_at, self.a.updated_at)

    def test_to_dict_Amenity(self):
        """test if dictionary works"""
        self.assertEqual('to_dict' in dir(self.a), True)


if __name__ == "__main__":
    unittest.main()
