from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Contact
from django.http import HttpResponse


@login_required
def contacts(request):
    if request.method=="POST":
        contact=Contact()
        firstname = request.POST.get('firstname')
        lastname = request.POST.get('lastname')
        email = request.POST.get('email')
        number = request.POST.get('number')
        subject = request.POST.get('subject')
        contact.firstname=firstname
        contact.lastname=lastname
        contact.email=email
        contact.number=number
        contact.subject=subject
        contact.save()
    return render(request,'contacts/contacts.html')
# Create your views here.
