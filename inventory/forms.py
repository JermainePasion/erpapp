from django.forms import ModelForm
from .models import Inventory
from django import forms

class AddInventoryForm(ModelForm):

    name = forms.CharField(widget=forms.TextInput(attrs={
        "class": "input",
        "type": "text",
        "placeholder": "enter product..."
    }))

    cost_per_item = forms.DecimalField(widget=forms.NumberInput(attrs={
        "class": "input",
        "type": "integer",
        "placeholder": "enter cost per item..."
    }))

    quantity_in_stock = forms.IntegerField(widget=forms.TextInput(attrs={
        "class": "input",
        "type": "integer",
        "placeholder": "enter quantity in stock.."
    }))

    quantity_sold = forms.IntegerField(widget=forms.TextInput(attrs={
        "class": "input",
        "type": "integer",
        "placeholder": "enter amount sold..."


    }))
    sales = forms.DecimalField(widget=forms.TextInput(attrs={
        "class": "input",
        "type": "integer",
        "placeholder": "enter sales/revenue"

    }))
    class Meta:
        model = Inventory
        fields = ['name', 'cost_per_item', 'quantity_in_stock', 'quantity_sold', 'sales']


class UpdateInventoryForm(ModelForm):
    class Meta:
        model = Inventory
        fields = ['name', 'cost_per_item', 'quantity_in_stock', 'quantity_sold', 'sales']
