from django.shortcuts import render
from orders.models import Orders
from django.contrib.auth.decorators import login_required

@login_required
def invoice (request):
    orders = Orders.objects.all()
    context = {
        "title": "Inventory List",
        "orders": orders
    }
    return render(request, 'invoice/invoice.html', context=context)

def render_invoice(request):
    return render(request, 'invoice/render_invoice.html')