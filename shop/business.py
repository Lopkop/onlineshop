import logging

from typing import Union

from django.shortcuts import HttpResponse
from django.utils.functional import SimpleLazyObject

from cloudipsp import Api, Checkout

from .models import ShoppingCart, ShoppingItem, Product

# Logging configuration
logger = logging.getLogger('project')


def add_product_to_shop(user: SimpleLazyObject, product: dict) -> None:
    """Adds product to the shop"""
    Product.objects.create(user=user, title=product['title'], description=product['description'],
                           category=product['category'],
                           price=product['price'])
    logger.info(f'{user} added new product => {product["title"]}')


def edit_product(pk: int, data: dict) -> None:
    """Edits product"""
    product = Product.objects.get(pk=pk)
    product.title = data.get('title')
    product.category = data.get('category', product.category)
    product.description = data.get('description', product.description)
    product.price = data.get('price', product.price)
    product.save()
    logger.info(f'{product} edited')


def remove_product_from_shop(user: SimpleLazyObject, pk: int) -> Union[HttpResponse]:
    """Removes item from shop if it exists"""
    try:
        product = Product.objects.get(pk=pk)
    except Product.DoesNotExist:
        return HttpResponse(f'Some error occurred while removing product from shop.')
    if user == product.user:
        product.delete()
    else:
        logger.warning(f'{user} tried to remove product from shop and failed!!!')


def add_item_to_shopping_cart(user: SimpleLazyObject, product: Product) -> None:
    """Adds item to shopping cart"""
    user_shopping_cart, _ = ShoppingCart.objects.get_or_create(user=user)
    shopping_item, flag = ShoppingItem.objects.get_or_create(user=user, product=product,
                                                             shopping_cart=user_shopping_cart)

    if flag:
        logger.info(f'{user_shopping_cart} added to shopping cart this item => {shopping_item}')


def remove_item_from_shopping_cart(user: SimpleLazyObject, pk: int) -> Union[HttpResponse]:
    """Removes item from shopping cart if it exists"""
    try:
        item = ShoppingItem.objects.get(pk=pk)
    except ShoppingItem.DoesNotExist:
        return HttpResponse(f'Some error occurred while removing item from shopping cart.')
    if user == item.user:
        item.delete()


def get_url_from_api_to_buy_item(pk: int) -> Checkout:
    """Request to the fondy API and returns checkout url"""
    api = Api(merchant_id=1396424,
              secret_key='test')
    checkout = Checkout(api=api)
    data = {
        "currency": "USD",
        "amount": f'{int(ShoppingItem.objects.get(pk=pk).product.price)}00'
    }
    return checkout.url(data).get('checkout_url')
