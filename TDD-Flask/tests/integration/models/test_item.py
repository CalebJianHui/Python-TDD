from models.item import ItemModel
from tests.base_test import BaseTest


class ItemTest(BaseTest):
    def test_crud(self):
        with self.app_context():
            item = ItemModel('test', 19.92)
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
