from django.forms import ModelForm
from .models import Orders
from django import forms

class AddOrderForm(ModelForm):

    description = forms.CharField(widget=forms.TextInput(attrs={
        "class": "input",
        "type": "text",
        "placeholder": "enter product..."
    }))

    quantity = forms.CharField(widget=forms.TextInput(attrs={
        "class": "input",
        "type": "integer",
        "placeholder": "enter amount..."
    }))

    price = forms.CharField(widget=forms.TextInput(attrs={
        "class": "input",
        "type": "integer",
        "placeholder": "enter price..."
    }))

    warehouse= forms.CharField(widget=forms.TextInput(attrs={
        "class": "input",
        "type": "text",
        "placeholder": "enter warehouse..."
    }))

    class Meta:
        model = Orders
        fields = ['description', 'quantity', 'price', 'warehouse']