from TDD_Flask.models.store import StoreModel
from TDD_Flask.tests.unit.test_unit_base import UnitBaseTest


class StoreTest(UnitBaseTest):
    def test_create_store(self):
        store = StoreModel('test')

        self.assertEqual(store.name, 'test',
                         "The name of the store after creation does not match the constructor argument")
