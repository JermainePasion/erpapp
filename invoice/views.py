from django.shortcuts import render, redirect
from orders.models import Orders
from django.contrib.auth.decorators import login_required
from django.core.mail import BadHeaderError, send_mail
from django.template.loader import  render_to_string
from django.http import HttpResponse, HttpResponseRedirect
from django.utils.html import strip_tags
from django.conf import settings
from django.shortcuts import get_object_or_404


@login_required
def invoice (request):
    orders = Orders.objects.all()
    context = {
        "title": "Inventory List",
        "orders": orders
    }
    return render(request, 'invoice/invoice.html', context=context)

def render_invoice(request, pk):
    obj = get_object_or_404(Orders, pk=pk)
    subject = (obj.warehouse)
    email = (obj.user.email)
    name = (obj.user)
    print(subject, email, name)

    if request.method == 'POST':
        message = request.POST.get('message')
        message_data = {
            'subject': subject,
            'email': email,
            'name': name,
        }
        html_message = render_to_string('invoice/email_invoice.html', message_data)
        plain_message = strip_tags(html_message)

        if subject and message and email:
            try:
                send_mail(subject, plain_message, settings.EMAIL_HOST_USER, [email], html_message=html_message)
            except BadHeaderError:
                return HttpResponse('Invalid header found.')
            return redirect('invoice')
        else:
            return HttpResponse('Make sure all fields are entered and valid.')

    context = {
        'subject': subject,
        'email': email,
         'name': name,
    }
    return render(request, 'invoice/render_invoice.html', context)

# def send_email_to_client():
#     subject = 'This is an email from django'
#     message = 'Hello World'
#     from_email = settings.EMAIL_HOST_USER
#     recepient_list = ['mainejerms@gmail.com']
#     send_mail(subject, message, from_email, recepient_list)
#
# def send_email(request, pk):
#     send_email_to_client()
#     return redirect('invoice')