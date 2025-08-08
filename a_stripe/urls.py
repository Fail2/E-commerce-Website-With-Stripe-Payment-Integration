from django.urls import path
from .views import *

urlpatterns=[
    path('', shop_view, name='shop'),
    path('cart/',cart_view, name='cart'),
    path('product/<product_id>/',product_view, name='product'),
    path('payment-successful/', payment_successful, name='payment_successful'),
    path('payment-cancelled/', payment_cancelled, name='payment_cancelled'),
    path('stripe/ebhook/',stripe_webhook, name='stripe_webhook'),
    path('add_to_cart/<product_id>/', add_to_cart, name='add_to_cart'),
    path('hx-menu-cart/', hx_menu_cart, name='hx_menu_cart'),
    path('update_cart/<product_id>/', update_checkout, name='update_checkout'),
    path('remove_from_cart/<product_id>/', remove_from_cart, name='remove_from_cart'),
    path('checkout/', checkout_view, name='checkout'),
]