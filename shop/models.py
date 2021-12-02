import decimal

from django.core.validators import MinValueValidator
from django.contrib.auth.models import User
from django.db import models

from .configs import categories


class Product(models.Model):
    """Product model represents product information"""
    title = models.CharField(max_length=255)
    category = models.CharField(max_length=20, choices=categories)
    description = models.TextField(max_length=4096)
    price = models.DecimalField(max_digits=15, decimal_places=2,
                                validators=[MinValueValidator(decimal.Decimal(0.00))])
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title


class ShoppingCart(models.Model):
    """Shopping cart model for products that user want to buy"""
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.user)


class ShoppingItem(models.Model):
    """Product that user want to buy"""
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    shopping_cart = models.ForeignKey(ShoppingCart, on_delete=models.CASCADE, related_name='items')
    product = models.ForeignKey(Product, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.product)
