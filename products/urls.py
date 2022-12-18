from django.urls import path
from django.views.generic import TemplateView
from .views import *

urlpatterns = [
    path('add/', addproduct, name='add_product'),
    path('', ProductListView.as_view(), name='product_list'),
    path('<slug:slug>/', ProductDetailView.as_view(), name='product_detail'),
]