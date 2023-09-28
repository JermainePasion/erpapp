from django.shortcuts import render, redirect

def contacts(request):
    return render(request,'contacts/contacts.html')
# Create your views here.
