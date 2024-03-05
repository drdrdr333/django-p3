from django.test import TestCase
from django.contrib.auth.models import User
from blogging.models import Post, Category
import datetime
from django.utils.timezone import utc

# Create your tests here.
class PostTestCase(TestCase):
    fixtures = ['blogging_test_fixtures.json']

    def setUp(self):
        self.user = User.objects.get(pk=1)
    
    def test_string_representation(self):
        expected = "first post"
        p1 = Post(title=expected)
        actual = str(p1)
        self.assertEqual(expected, actual)


class CategoryTestCase(TestCase):
    def test_string_repr(self):
        expected = "A Category"
        c1_test = Category(name=expected)
        actual = str(c1_test)
        self.assertEquals(expected, actual)

class FrontEndTestCase(TestCase):
    ''' test views provided in the front end '''
    fixtures = ['blogging_test_fixtures.json']

    def setUp(self):
        self.now = datetime.datetime.utcnow().replace(tzinfo=utc)
        self.timedelta = datetime.timedelta(15)
        author = User.objects.get(pk=1)
        for count in range(1, 11):
            post = Post(title=f"Post {count} Title",
                        text='Foo',
                        author=author)
            if count < 6:
                pubdate = self.now - self.timedelta * count
                post.published_date = pubdate
            post.save()
    
    def test_list_only_published(self):
        resp = self.client.get('/')
        # the content of the rendered response is always a bytestring
        resp_text = resp.content.decode(resp.charset)
        self.assertTrue("Recent posts" in resp_text)
        # helper = Post.objects.all()
        # print(helper)
        for count in range(1, 11):
            title = "Post %d Title" % count
            if count < 6:
                self.assertContains(resp, title, count=1)
            else:
                self.assertNotContains(resp, title)

    def test_details_only_published(self):
        for count in range(1, 11):
            title = f"Post {count} Title"
            post = Post.objects.get(title=title)
            resp = self.client.get(f"/posts/{count}/")
            if count < 6:
                self.assertEqual(resp.status_code, 200)
                self.assertContains(resp, title)
            else:
                self.assertEqual(resp.status_code, 404)
