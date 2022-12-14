from unittest import TestCase
from TDD_CLI.blog import Blog


class BlogTest(TestCase):
    def test_create_post(self):
        b = Blog('Test', 'Test Author')
        b.create_post("Popz title", "many content")

        self.assertEqual(len(b.posts), 1)
        self.assertEqual(b.posts[0].title, 'Popz title')
        self.assertEqual(b.posts[0].content, 'many content')

    def test_json_no_posts(self):
        b = Blog('Test', 'Test Author')
        expected = {'title': 'Test', 'author': 'Test Author', 'posts': []}

        self.assertDictEqual(expected, b.json())

    def test_json(self):
        b = Blog('Test', 'Test Author')
        b.create_post("Popz title", "many content")

        expected = {
            'title': 'Test',
            'author': 'Test Author',
            'posts': [
                {
                    'title': 'Popz title',
                    'content': 'many content',
                }
            ],
        }

        self.assertDictEqual(expected, b.json())
