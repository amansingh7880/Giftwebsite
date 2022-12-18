from django.urls import path
from .views import *
from django.contrib.auth.decorators import login_required

urlpatterns = [
    path('login/', login_view, name = 'login'),
    path('register/', register_view, name = 'register'),
    path('logout/',logout, name='logout'),
]