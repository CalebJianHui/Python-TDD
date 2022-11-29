from unittest import TestCase

from TDD_Flask.models.item import ItemModel


class ItemTest(TestCase):
    def test_create_item(self):
        item = ItemModel("Mochi", 10)

        self.assertEqual("Mochi", item.name,
                         "The name of the item after init does not match the constructor argument.")
        self.assertEqual(10, item.price,
                         "The price of the item after init does not match the constructor argument.")

    def test_item_json(self):
        item = ItemModel("Mochi", 10.90)
        expected = {
            "name": "Mochi",
            "price": 10.90
        }

        self.assertEqual(item.json(), expected,
                         "The json export of the item is incorrect. Received {}, expected {}".format(item.json(),
                                                                                                     expected))
