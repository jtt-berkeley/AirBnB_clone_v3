import unittest
import os

os.environ["FS_TEST"] = "yes"

from datetime import datetime
from models import *


class Test_AmenityModel(unittest.TestCase):
    """
    Test the amenity model class
    """

    def setUp(self):
        """set up before running any test"""
        test_args = {'updated_at': datetime(2017, 2, 12, 00, 31, 53, 331997),
                     'id': 'f519fb40-1f5c-458b-945c-2ee8eaaf4900',
                     'created_at': datetime(2017, 2, 12, 00, 31, 53, 331900),
                     'name': "AMENITY SET UP"}
        self.model = Amenity(**test_args)
        self.model.save()

    def tearDown(self):
        """tear down after every test"""
        storage.delete(self.model)

    def tearDownModule():
        """tear down as leaving the module"""
        os.environ["TEST_FS"] = "no"

    def test_var_initialization(self):
        """test the creation of the model went right"""
        self.assertEqual(self.model.name, "AMENITY SET UP")

    def test_missing_arg(self):
        """test creating an Amenity with no argument"""
        new = Amenity()
        self.assertTrue(hasattr(new, "id"))
        self.assertTrue(hasattr(new, "name"))

    def test_date_format(self):
        """test the date has the right type"""
        self.assertIsInstance(self.model.created_at, datetime)


if __name__ == "__main__":
    unittest.main()
