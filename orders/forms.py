from django import forms

from .models import OrderItem, Order

class CheckoutForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = '__all__'