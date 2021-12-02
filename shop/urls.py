from django.urls import path
from .views import (
    product_list_view,
    shopping_cart_view,
    product_detail_view,
    remove_item_view,
    buy_item_view,
    user_product_list_view,
    add_product_view,
    remove_product_view,
    edit_product_view,
    setting_product_view,
)

urlpatterns = [
    path('', product_list_view, name='shop'),
    path('shopping_cart/', shopping_cart_view, name='shopping_cart'),
    path('<int:pk>/', product_detail_view, name='product'),
    path('remove-from-shopping-cart/<int:pk>/', remove_item_view,
         name='remove_from_shopping_cart'),
    path('buy-item/<int:pk>/', buy_item_view, name='buy_item'),

    # Add, edit, remove products
    path('my-products/add-new-product/', add_product_view, name='add_new_product'),
    path('my-products/setting-product/<int:pk>/', setting_product_view, name='setting_product'),
    path('my-products/edit-product/<int:pk>/', edit_product_view, name='edit_product'),
    path('my-products/remove-product/<int:pk>/', remove_product_view, name='remove_product'),
    path('my-products/', user_product_list_view, name='my_products'),
]
