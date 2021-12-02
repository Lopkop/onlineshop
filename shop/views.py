import logging

from django.core import exceptions
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, HttpResponseRedirect, reverse

from shop.models import Product, ShoppingItem
from .business import (
    add_item_to_shopping_cart,
    remove_item_from_shopping_cart,
    get_url_from_api_to_buy_item,
    add_product_to_shop,
    edit_product,
    remove_product_from_shop,
)
from .forms import ProductForm

logger = logging.getLogger('project')


def product_list_view(request):
    return render(request, 'shop/product_list.html', {'products': Product.objects.order_by('-pk')})


def product_detail_view(request, pk):
    product = Product.objects.get(pk=pk)
    if request.method == 'POST':
        if request.user.is_authenticated:
            add_item_to_shopping_cart(request.user, product)
            return HttpResponseRedirect(reverse('shop'))
        else:
            return HttpResponseRedirect(reverse('login'))
    return render(request, 'shop/product_detail.html', {'product': product})


@login_required(login_url='/accounts/login/')
def user_product_list_view(request):
    return render(request, 'shop/user_product_list.html', {'products': Product.objects.filter(user=request.user)})


@login_required(login_url='/accounts/login/')
def add_product_view(request):
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            add_product_to_shop(request.user, form.cleaned_data)
            return HttpResponseRedirect(reverse('my_products'))
    return render(request, 'shop/add_new_product.html', {'form': ProductForm})


@login_required(login_url='/accounts/login/')
def setting_product_view(request, pk):
    product = Product.objects.get(pk=pk)
    if request.user == product.user:
        return render(request, 'shop/user_product_detail.html',
                      {'product': product})
    logger.debug(f'{request.user} access denied')
    raise exceptions.PermissionDenied()


@login_required(login_url='/accounts/login/')
def edit_product_view(request, pk):
    product = Product.objects.get(pk=pk)
    if product.user == request.user:
        if request.method == 'POST':
            form = ProductForm(request.POST)
            if form.is_valid():
                edit_product(pk, form.cleaned_data)
                return HttpResponseRedirect(reverse('my_products'))
        return render(request, 'shop/edit_product.html',
                      {'form': ProductForm({'title': product, 'category': product.category,
                                            'description': product.description,
                                            'price': product.price})})
    logger.debug(f'{request.user} access denied')
    raise exceptions.PermissionDenied()


@login_required(login_url='/accounts/login/')
def remove_product_view(request, pk):
    remove_product_from_shop(request.user, pk)
    return HttpResponseRedirect(reverse('my_products'))


def shopping_cart_view(request):
    return render(request, 'shop/shopping_cart.html',
                  {'shopping_items': ShoppingItem.objects.order_by('-pk')})


def remove_item_view(request, pk):
    remove_item_from_shopping_cart(request.user, pk)
    return HttpResponseRedirect(reverse('shopping_cart'))


def buy_item_view(request, pk):
    url = get_url_from_api_to_buy_item(pk)
    return HttpResponseRedirect(url)
