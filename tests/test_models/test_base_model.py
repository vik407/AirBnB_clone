#!/usr/bin/python3
"""BaseModel test file
"""
# imports
import unittest
import os
import pep8
# import models
from models.base_model import BaseModel
# ...


class TestBaseModel(unittest.TestCase):
    """Set the test for base model class
    """
    # First things first, the setupclass
    @classmethod
    def setUpClass(cls):
        """Called before test in an individual class are run
        """
        cls.b = BaseModel()
        cls.b.save()

    @classmethod
    def tearDown(cls):
        """Called after test in an individual class have run
        """
        del cls.b

    # Clean after run tests
    def tearDown(self):
        """Clean file created after run the test (json file)
        """
        try:
            os.remove("file.json")
        except FileNotFoundError:
            pass

    # Run pep8 validate console.py
    def test_base_model_py(self):
        """pep8 base_model.py test
        """
        s = pep8.StyleGuide(quiet=True)
        f = s.check_files(['models/base_model.py'])
        self.assertEqual(s.total_errors, 0, 'pep8 error found!')

    # Docstrings
    def test_docstrings_base_model(self):
        """Find docstrings on base_model file
        """
        self.assertIsNotNone(BaseModel.__doc__)
        self.assertIsNotNone(BaseModel.__init__.__doc__)
        self.assertIsNotNone(BaseModel.__str__.__doc__)
        self.assertIsNotNone(BaseModel.save.__doc__)
        self.assertIsNotNone(BaseModel.to_dict.__doc__)

    # Test Save
    def test_save_base_model(self):
        """Test the save method
        """
        self.b.save()
        self.assertEqual(self.b.updated_at, self.b.created_at)

    # Test to_dict
    def test_to_dict_base_model(self):
        """Test to_dict
        """
        test_dict = self.b.to_dict()
        self.assertEqual(self.b.__class__.__name__, 'BaseModel')
        self.assertIsInstance(test_dict['created_at'], str)
        self.assertIsInstance(test_dict['updated_at'], str)

    # Instance creation (BaseModel)
    def test_instance_basemodel(self):
        """Instance creation check
        """
        self.assertTrue(isinstance(self.base, BaseModel))

    # Check class for the listing methods
    def test_methods_base_model(self):
        """Find methods on base_model file
        """
        self.assertTrue(hasattr(BaseModel, "__init__"))
        self.assertTrue(hasattr(BaseModel, "__str__"))
        self.assertTrue(hasattr(BaseModel, "save"))
        self.assertTrue(hasattr(BaseModel, "to_dict"))

if __name__ == "__main__":
    unittest.main()
