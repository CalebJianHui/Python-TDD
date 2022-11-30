from TDD_Flask.tests.unit.test_unit_base import UnitBaseTest

from TDD_Flask.models.item import ItemModel


# Update pyJWT should you face any issue
class ItemTest(UnitBaseTest):
    def test_create_item(self):
        item = ItemModel("Mochi", 10, 1)

        self.assertEqual("Mochi", item.name,
                         "The name of the item after init does not match the constructor argument.")
        self.assertEqual(10, item.price,
                         "The price of the item after init does not match the constructor argument.")
        self.assertEqual(item.store_id, 1)
        self.assertIsNone(item.store)

    def test_item_json(self):
        item = ItemModel("Mochi", 10.90, 1)
        expected = {
            "name": "Mochi",
            "price": 10.90
        }

        self.assertEqual(item.json(), expected,
                         "The json export of the item is incorrect. Received {}, expected {}".format(item.json(),
                                                                                                     expected))
