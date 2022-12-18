from django.urls import path
from django.views.generic import TemplateView
from .views import *

urlpatterns = [
    path('add/', addproduct, name='add_product'),
    path('', ProductListView.as_view(), name='product_list'),
    path('<slug:slug>/', ProductDetailView.as_view(), name='product_detail'),
    path('cart/add/', add_to_cart, name='add_to_cart'),
    path('cart/remove/<int:id>', remove_from_cart, name='remove_from_cart'),
    path('cart/show', show_cart, name='show_cart'),
    path('search/', search, name='search'),
    path('cart/checkout', checkout, name='checkout'),
]