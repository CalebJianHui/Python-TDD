"""
BaseTest

This class is the parent class to each non-unit test.
Allows for instantiation of the database dynamically
and makes sure that it is a new, blank database each time.
"""
from unittest import TestCase
from TDD_Flask.app import app
from TDD_Flask.db import db


class IntegrationBaseTest(TestCase):
    def setUp(self):
        # Make sure database exist
        # - For this project, we shall simply use sqlite,
        # - For production, we should use a similar database that is used in production
        app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///'
        with app.app_context():
            db.init_app(app)
            db.create_all()
        # Get a test client
        self.app = app.test_client()
        self.app_context = app.app_context

    def tearDown(self):
        # Empty database
        with app.app_context():
            db.session.remove()
            db.drop_all()
