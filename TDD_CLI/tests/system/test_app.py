from unittest import TestCase
from unittest.mock import patch
from TDD_CLI import app
from TDD_CLI.blog import Blog
from TDD_CLI.post import Post


class AppTest(TestCase):
    def setUp(self) -> None:
        blog = Blog('Test', 'Test Author')
        app.blogs = {'Test': blog}

    def test_menu_display_prompt(self):
        with patch('builtins.input', return_value='q') as mocked_input:
            app.menu()
            mocked_input.assert_called_with(app.MENU_PROMPT)

    def test_menu_calls_create_blog(self):
        with patch('builtins.input') as mocked_input:
            with patch('app.prompt_create_blog') as mocked_prompt_create_blog:
                mocked_input.side_effect = ('c', 'q')

                app.menu()
                mocked_prompt_create_blog.assert_called()

    def test_menu_call_print_blogs(self):
        with patch('app.print_blogs') as mocked_print:
            # Patch input call to ignore user input and assign a value
            with patch('builtins.input', return_value='q'):
                app.menu()
                mocked_print.assert_called()

    def test_print_blogs(self):
        with patch('builtins.print') as mocked_print:
            app.print_blogs()
            mocked_print.assert_called_with('- Test by Test Author (0 post)')

    def test_prompt_create_blog(self):
        with patch('builtins.input') as mocked_input:
            # Allow multiple line input
            mocked_input.side_effect = ('Test', 'Test Author')
            app.prompt_create_blog()

            self.assertIsNotNone(app.blogs.get('Test'))

    def test_prompt_read_blog(self):
        with patch('builtins.input', return_value='Test') as mocked_input:
            with patch('app.print_posts') as mocked_print_posts:
                app.prompt_read_blog()

                mocked_print_posts.assert_called_with(app.blogs['Test'])

    def test_print_posts(self):
        app.blogs['Test'].create_post('Test Post', 'Test Content')

        with patch('app.print_post') as mocked_print_post:
            app.print_posts(app.blogs['Test'])

            mocked_print_post.assert_called_with(app.blogs['Test'].posts[0])

    def test_print_post(self):
        post = Post('Post title', 'Post content')
        expected_print = '''
--- Post title ---

Post content
'''
        with patch('builtins.print') as mocked_print:
            app.print_post(post)

            mocked_print.assert_called_with(expected_print)

    def test_ask_create_post(self):

        with patch('builtins.input') as mocked_input:
            mocked_input.side_effect = ('Test', 'Test Title', 'Test Content')

            app.prompt_create_post()

            self.assertEqual(app.blogs['Test'].posts[0].title, 'Test Title')
            self.assertEqual(app.blogs['Test'].posts[0].content, 'Test Content')
