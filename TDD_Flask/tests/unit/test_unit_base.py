from TDD_Flask.app import app
from unittest import TestCase


# To allow importing of Store via App without init and teardown
class UnitBaseTest(TestCase):
    pass
