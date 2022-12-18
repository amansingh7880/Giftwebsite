from django import forms
from .models import ProductItem

class ProductForm(forms.ModelForm):
    class Meta:
        model = ProductItem
        fields = ['image','title', 'description', 'price', 'summary', 'featured']