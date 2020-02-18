#!/usr/bin/python3
"""BaseModel test file
"""
# imports
import unittest
import os
import pep8
# import models
from models.base_model import BaseModel
from models.amenity import Amenity
# ...


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
        self.assertEqual(s.total_errors, 0, 'pep8 error found!')

    # Docstrings
    def test_docstrings_amenity(self):
        """Find docstrings on amenity file
        """
        self.assertIsNotNone(Amenity.__doc__)

    # Attributes
    def test_amenity_attributes(self):
        """Validate attrs
        """
        self.assertTrue('id' in self.amenity.__dict__)
        self.assertTrue('created_at' in self.amenity.__dict__)
        self.assertTrue('updated_at' in self.amenity.__dict__)
        self.assertTrue('name' in self.amenity.__dict__)

    def test_amenity_subclass(self):
        """Valitate if comes from BaseModel - subclass
        """
        self.assertTrue(issubclass(self.amenity.__class__, BaseModel), True)

    # Check class for the listing methods
    def test_attribute_amenity(self):
        """Validate if comes name on amenity
        """
        self.assertEqual(type(self.amenity.name), str)

    def test_amenity_save(self):
        """Save method works?
        """
        self.amenity.save()
        self.assertNotEqual(self.amenity.created_at, self.amenity.updated_at)

    def test_amenity_to_dict(self):
        """to dict works?
        """
        self.assertEqual('to_dict' in dir(self.amenity), True)

if __name__ == "__main__":
    unittest.main()
