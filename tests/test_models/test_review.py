import unittest
from datetime import datetime
from models import *


class Test_ReviewModel(unittest.TestCase):
    """
    Test the review model class
    """

    def test_initialization_no_arg(self):
        """test simple initialization with no arguments"""
        model = Review()
        self.assertTrue(hasattr(model, "place_id"))
        self.assertTrue(hasattr(model, "user_id"))
        self.assertTrue(hasattr(model, "text"))
        self.assertTrue(hasattr(model, "id"))
        self.assertTrue(hasattr(model, "created_at"))

    def test_var_initialization(self):
        """Check default type"""
        model = Review()
        self.assertIsInstance(model.created_at, datetime)

    def test_save(self):
        """saving the object to storage"""
        test_user = {'id': "001",
                     'email': "you@g.com",
                     'password': "1234",
                     'first_name': "TEST",
                     'last_name': "REVIEW"}
        user = User(test_user)
        test_state = {'id': "001",
                      'created_at': datetime(2017, 2, 12, 00, 31, 55, 331997),
                      'name': "TEST STATE FOR CITY"}
        state = State(test_state)
        state.save()
        test_city = {'id': "005",
                     'name': "CITY SET UP",
                     'state_id': "001"}
        city = City(test_city)
        test_place = {'id': "003",
                      'city_id': "005",
                      'user_id': "001",
                      'name': "TEST REVIEW",
                      'description': "blah blah",
                      'number_rooms': 4,
                      'number_bathrooms': 2,
                      'max_guest': 4,
                      'price_by_night': 23,
                      'latitude': 45.5,
                      'longitude': 23.4}
        place = Place(test_place)
        test_review = {'text': "a text",
                       'place_id': "003",
                       'user_id': "001"}
        review = Review(test_review)
        user.save()
        state.save()
        city.save()
        place.save()
        review.save()
        storage.delete(review)
        storage.delete(place)
        # storage.delete(city) cascade deletes it
        storage.delete(user)
        storage.delete(state)


if __name__ == "__main__":
    unittest.main()
