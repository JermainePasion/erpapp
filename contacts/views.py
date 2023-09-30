from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required



@login_required
def contacts(request):
    return render(request,'contacts/contacts.html')
# Create your views here.
