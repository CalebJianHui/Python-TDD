from unittest import TestCase
from post import Post


class PostTest(TestCase):
    def test_create_post(self):
        p = Post('Test title', 'Test Content')

        self.assertEqual('Test title', p.title)
        self.assertEqual('Test Content', p.content)

    def test_json(self):
        p = Post('Test title', 'Test Content')
        expected = {'title': 'Test title', 'content': 'Test Content'}

        self.assertDictEqual(expected, p.json())
