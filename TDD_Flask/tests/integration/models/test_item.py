from TDD_Flask.models.item import ItemModel
from TDD_Flask.models.store import StoreModel
from TDD_Flask.tests.integration.test_integration_base import IntegrationBaseTest


class ItemTest(IntegrationBaseTest):
    def test_crud(self):
        with self.app_context():
            # SQLite do not enforce foreign key, but postgreSQL would enforce it
            # Adding a store first will allow the inclusion of foreign key
            StoreModel('test').save_to_db()

            item = ItemModel('test', 19.92, 1)
            # Ensure that the item does not exist already before saving
            self.assertIsNone(ItemModel.find_by_name('test'),
                              f"Found an item with name {item.name}, but expected not to.")

            # Save to DB
            item.save_to_db()
            self.assertIsNotNone(ItemModel.find_by_name('test'),
                                 f"Item {item.name} not saved to DB")

            # Delete from DB
            item.delete_from_db()
            self.assertIsNone(ItemModel.find_by_name('test'),
                              f"Item {item.name} not deleted from DB")

    def test_store_relationship(self):
        with self.app_context():
            store = StoreModel('test_store')
            item = ItemModel('test', 19.99, 1)

            store.save_to_db()
            item.save_to_db()

            self.assertEqual(item.store.name, 'test_store')
