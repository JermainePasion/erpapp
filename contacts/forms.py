from django.forms import ModelForm
from.models import Contact
from django import forms

class ContactForm(ModelForm):
    firstname = forms.CharField(widget=forms.TextInput(attrs={
        "class": "input",
        "type": "text",
        "placeholder": "Firstname"
    }))

    lastname = forms.CharField(widget=forms.NumberInput(attrs={
        "class": "input",
        "type": "text",
        "placeholder": "Lastname"
    }))

    email = forms.EmailField(widget=forms.TextInput(attrs={
        "class": "input",
        "type": "email",
        "placeholder": "Email"
    }))

    number = forms.IntegerField(widget=forms.TextInput(attrs={
        "class": "input",
        "type": "integer",
        "placeholder": "Your Phone Number"

    }))
    subject = forms.CharField(widget=forms.TextInput(attrs={
        "class": "input",
        "type": "text",
        "placeholder": "Your message"

    }))

    class Meta:
        model = Contact
        fields = ['firstname', 'lastname', 'email', 'number', 'subject']