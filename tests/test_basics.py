import unittest

from flask import current_app
from app import create_app, db

# This class inherits from unittest.
# @TODO: Read the documentation of unittest
class BasicsTestCase(unittest.TestCase):
    def setUp(self):
        # We need to recreate the environment of the app or a similar set
        # of conditions to execute our tests
        self.app = create_app('testing')
        # a context is necessary
        self.app_context = self.app.app_context()
        self.app_context.push()
        # and a testing database for sure
        db.create_all()
    def tearDown(self):
        db.session.remove()
        db.drop_all()
        self.app_context.pop()
    # Checks that the app exists
    def test_app_exists(self):
        self.assertFalse(current_app is None)
    # Checks that all tests are being executed with the right conifg
    def test_app_is_testing(self):
        self.assertTrue(current_app.config['testing'])