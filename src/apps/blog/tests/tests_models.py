from django.test import TestCase
from django.db.models import Subquery
from apps.blog.models import Category, Post
from apps.users.models import User


class CategoryModelTest(TestCase):

    @classmethod
    def setUpTestData(cls) -> None:
        cls.category = Category.objects.create(
            name="Gamedev",
            description="There are some news about gamedev in this category",
        )

    def test_str_dumper(self):
        category = self.category
        str_repr = str(category)

        self.assertEqual(str_repr, "Gamedev")

    def test_name_max_length(self):
        category = self.category
        max_length = category._meta.get_field("name").max_length

        self.assertEqual(max_length, 50)

    def test_managers_get_recent_posts_per_category(self):
        one_category = self.category

        another_category = Category.objects.create(
            name="Programming",
            description="Some news in programming industry",
        )

        some_author = User.objects.create(
            username="some_author",
            password="some_author",
        )

        latest_post_for_gamedev_category = Post.objects.create(
            author=some_author,
            title="The latest post in Gamedev",
            text="This post should be the last in category",
            category=one_category,
        )

        earlier_post_for_gamedev_category = Post.objects.create(
            author=some_author,
            title="Earlier post in Gamedev",
            text="This is a more recent post than the previous one",
            category=one_category,
        )

        one_post_for_another_category = Post.objects.create(
            author=some_author,
            title="First post in programming",
            text="This post is the latest",
            category=another_category,
        )

        another_post_for_another_category = Post.objects.create(
            author=some_author,
            title="Second post in programming",
            text="It should be seen before 'First post in programming'",
            category=another_category,
        )

        result_query = Category.objects.get_recent_posts_per_category()

        expected_query = [
            {
                "name": "Gamedev",
                "description": "There are some news about gamedev in this category",
                "slug": "gamedev",
                "recent_posts": [
                    {
                        "title": "Earlier post in Gamedev",
                        "text": "This is a more recent post than the previous one",
                        "slug": "earlier-post-in-gamedev",
                    },
                    {
                        "title": "The latest post in Gamedev",
                        "text": "This post should be the last in category",
                        "slug": "the-latest-post-in-gamedev",
                    },
                ],
            },
            {
                "name": "Programming",
                "description": "Some news in programming industry",
                "slug": "programming",
                "recent_posts": [
                    {
                        "title": "Second post in programming",
                        "text": "It should be seen before 'First post in programming'",
                        "slug": "second-post-in-programming",
                    },
                    {
                        "title": "First post in programming",
                        "text": "This post is the latest",
                        "slug": "first-post-in-programming",
                    },
                ],
            },
        ]

        self.assertEqual(list(result_query), expected_query)


class PostModelTest(TestCase):

    @classmethod
    def setUpTestData(cls) -> None:
        cls.author = User.objects.create(
            username="some_author",
            password="some_author",
        )
        cls.author.save()

        cls.category = Category.objects.create(
            name="Gamedev",
            description="There are some news about gamedev in this category",
        )
        cls.category.save()

        cls.post = Post.objects.create(
            author=cls.author,
            title="LoL",
            text="Have you seen that riot want to add Vanguard to the game?",
            category=cls.category,
        )

    def test_correct_foreign_key_in_category(self):
        post = self.post
        category_key = post.category

        category_object = self.category

        self.assertEqual(category_key, category_object)
        self.assertEqual(category_key.name, "Gamedev")

    def test_correct_foreign_key_for_author(self):
        post = self.post
        author_key = post.author

        author_object = self.author

        self.assertEqual(author_key, author_object)
        self.assertEqual(author_key.username, "some_author")

    def test_title_max_length(self):
        post = self.post
        max_length = post._meta.get_field("title").max_length

        self.assertEqual(max_length, 150)

    def test_autopopulated_slug_in_admin(self):
        post = self.post
        slug = post.slug

        self.assertEqual(slug, "lol")

    def test_unique_slug_on_save(self):

        post1 = Post.objects.create(
            author=self.author,
            title="LoL",
            text="Test if slug will change if you try to save it",
            category=self.category,
            slug="lol",
        )

        slug1 = post1.slug
        existing_slug = self.post.slug

        self.assertNotEqual(slug1, existing_slug)

    def test_unique_autopopulated_slug_on_creation(self):

        category = self.category
        author = self.author

        post1 = Post.objects.create(
            author=author,
            title="LoL",
            text="Another object with the same autogenerated slug but with 1 at the end",
            category=category,
        )
        slug1 = post1.slug

        self.assertEqual(slug1, "lol1")

        post2 = Post.objects.create(
            author=author,
            title="LoL",
            text="Yet another object with the same autogenerated slug but with 2 at the end",
            category=category,
        )
        slug2 = post2.slug

        self.assertEqual(slug2, "lol2")

    def test_managers_get_recent_posts_per_category_subquery(self):

        category = self.category
        author = self.author

        newer_post = Post.objects.create(
            author=author,
            title="LoL",
            text="Another object with the same autogenerated slug but with 1 at the end",
            category=category,
        )

        the_newest_post = Post.objects.create(
            author=author,
            title="LoL",
            text="Another object with the same autogenerated slug but with 1 at the end",
            category=category,
        )

        number_of_needed_recent_posts = 1
        result_subquery = Post.objects.get_recent_posts_per_category_subquery(
            limit=number_of_needed_recent_posts
        )
        testing_query = Category.objects.annotate(recent_post=Subquery(result_subquery))

        expected_query = []
        print(testing_query)
