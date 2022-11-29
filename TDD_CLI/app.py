from blog import Blog

MENU_PROMPT = "Enter 'c' to create a blog entry, 'l' to list blogs, 'r' to read one, 'p' to create a post, or 'q' " \
              "to quit"
POST_TEMPLATE = '''
--- {} ---

{}
'''

blogs = dict()


def menu():
    print_blogs()
    selection = input(MENU_PROMPT)
    while selection != 'q':
        if selection == 'c':
            prompt_create_blog()
        elif selection == 'l':
            print_blogs()
        elif selection == 'r':
            prompt_read_blog()
        elif selection == 'p':
            prompt_create_post()
        selection = input(MENU_PROMPT)


def prompt_create_blog():
    title = input("Enter your blog title:")
    author = input("Enter your name:")

    blogs[title] = Blog(title, author)


def print_blogs():
    for key, blog in blogs.items():
        print(f"- {blog}")


def prompt_read_blog():
    title = input('Enter the blog title you want to read:')

    print_posts(blogs[title])


def print_posts(blog):
    for post in blog.posts:
        print_post(post)


def print_post(post):
    print(POST_TEMPLATE.format(post.title, post.content))


def prompt_create_post():
    blog_name = input('Enter the blog title that you want to write a post in: ')
    title = input('Enter your post title: ')
    content = input('Enter your post content: ')

    blogs[blog_name].create_post(title, content)
