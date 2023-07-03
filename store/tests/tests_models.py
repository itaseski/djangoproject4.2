from django.test import TestCase

from store.models import Category, Product
from django.contrib.auth.models import User


class CategoryModelTestCase(TestCase):

    def setUp(self):
        Category.objects.create(name="Python", slug="python")

    def test_creating_category(self):
        """
        Test Category model data insertion
        """
        data = Category.objects.get(name="Python")
        self.assertTrue(isinstance(data, Category))

    def test_str_representation(self):
        """
        Test Category model convert an object into the string representation. 
        """
        data = Category.objects.get(name="Python")        
        self.assertEqual(str(data), 'Python')   

class ProductModelTestCase(TestCase):

    def setUp(self):
        Category.objects.create(name="Python", slug="python")
        User.objects.create(username="admin")
        Product.objects.create(category_id=1, title="Learning Python", created_by_id=1, author="Mark Lutz", description="Best Python 3 book", slug="learning-python", image="learning-python", price="20.00")

    def test_creating_product(self):
        """
        Test Product model data insertion
        """
        data = Product.objects.get(title="Learning Python")
        self.assertTrue(isinstance(data, Product))

    def test_str_representation(self):
        """
        Test Product model convert an object into the string representation. 
        """
        data = Product.objects.get(title="Learning Python")
        self.assertEqual(str(data), 'Learning Python')   