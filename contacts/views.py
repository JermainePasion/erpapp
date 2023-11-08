from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Contact
from django.http import HttpResponse
from .forms import ContactForm
from django.contrib import messages

@login_required
def contacts(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Your concern has been sent. Please wait for our response, Thank you!")
            return redirect('contacts')
    else:
        form = ContactForm()
    return render(request, 'contacts/contacts.html', {'form': form})
# Create your views here.
