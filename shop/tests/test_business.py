from django.contrib.auth.models import User
from django.test import TestCase

from ..business import add_item_to_shopping_cart, remove_item_from_shopping_cart, add_product_to_shop, \
    remove_product_from_shop, edit_product
from ..models import Product, ShoppingItem, ShoppingCart


class TestBusinessLogic(TestCase):
    def setUp(self):
        self.user = User.objects.create(username='test', password='test123')
        self.product = Product.objects.create(title='TEST', description='test-test',
                                              category='books', price=18.00, user=self.user)
        self.user_cart, _ = ShoppingCart.objects.get_or_create(user=self.user)

    def test_add_item_to_shop(self):
        product = {'title': 'BMV 5', 'description': 'black car',
                   'category': 'cars', 'price': 110.00}
        add_product_to_shop(self.user, product)
        Product.objects.get(user=self.user, title=product.get('title'), category=product.get('category'))

    def test_remove_shop_item(self):
        remove_product_from_shop(self.user, self.product.pk)
        with self.assertRaisesMessage(expected_exception=Product.DoesNotExist):
            Product.objects.get(user=self.user, title='TEST', description='test-test',
                                category='books', price=18.00)

    def test_edit_shop_item(self):
        modified_product = {'title': 'blue car', 'price': 1453.00}
        edit_product(self.product.pk, modified_product)
        self.assertEqual('blue car', self.product.title)
        self.assertEqual(1453.00, self.product.price)

    def test_add_item_to_shopping_cart(self):
        add_item_to_shopping_cart(self.user, self.product)
        item = ShoppingItem.objects.get(user=self.user, shopping_cart=self.user_cart, product=self.product)
        self.assertEqual(str(self.product), str(item))

    def test_remove_item_from_shopping_cart(self):
        remove_item_from_shopping_cart(self.user, self.product.pk)
        with self.assertRaisesMessage(expected_exception=ShoppingItem.DoesNotExist,
                                      expected_message='ShoppingItem matching query does not exist.'):
            ShoppingItem.objects.get(user=self.user, shopping_cart=self.user_cart, product=self.product)
