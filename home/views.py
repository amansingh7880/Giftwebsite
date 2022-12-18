from django.shortcuts import render, redirect
from .models import Image
from django.views.generic import TemplateView

def Homeview(request):
     ctx = {}
     ctx['Image'] = Image.objects.all()
     ctx['title'] = 'Home'
     return render(request, 'home/index.html', ctx)