from unittest import skip

from django.test import Client, TestCase

from store.models import Category, Product


@skip("demonstrating skipping")
class TestSkip(TestCase):
    def test_skip_exmaple(self):
        pass

class TestViewResponses(TestCase):

    def setUp(self):
        self.c = Client()

    def test_url_allowed_hosts(self):
        """
        Test allowed hosts
        """
        response = self.c.get('/',)
        self.assertEqual(response.status_code, 200)