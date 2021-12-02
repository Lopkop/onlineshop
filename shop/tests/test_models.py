from django.contrib.auth.models import User
from django.test import TestCase

from ..models import Product, ShoppingItem, ShoppingCart


class TestProduct(TestCase):
    def setUp(self):
        self.user = User.objects.create(username='test', password='test123')
        self.product = Product.objects.create(title='TEST', description='test-test',
                                              category='books', price=18.00, user=self.user)

    def test_string_representation(self):
        self.assertEqual('TEST', self.product)


class TestShoppingCart(TestCase):
    def setUp(self):
        self.user = User.objects.create(username='test', password='test123')
        self.product = Product.objects.create(title='TEST', description='test-test',
                                              category='books', price=18.00, user=self.user)
        self.user_cart, _ = ShoppingCart.objects.get_or_create(user=self.user)

    def test_string_representation_returns_user_name(self):
        self.assertEqual('test', self.user_cart)


class TestShoppingItem(TestCase):
    def setUp(self):
        self.user = User.objects.create(username='test', password='test123')
        self.product = Product.objects.create(title='TEST', description='test-test',
                                              category='books', price=18.00, user=self.user)
        self.user_cart, _ = ShoppingCart.objects.get_or_create(user=self.user)

    def test_save_and_retrieve_item(self):
        item = ShoppingItem(user=self.user, product=self.product, shopping_cart=self.user_cart)
        print(ShoppingItem.objects.get(user=self.user))
