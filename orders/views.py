from django.shortcuts import render, redirect
from .models import Orders
from .forms import AddOrderForm
from django.contrib.auth.decorators import login_required


@login_required
def orders_list (request):
    orders = Orders.objects.all()
    context = {
        "title": "Inventory List",
        "orders": orders
    }
    return render (request, 'orders/orders_list.html', context=context)

def add(request):
   if request.method == 'POST':
       form = AddOrderForm(request.POST)
       if form.is_valid():
           form.save()
           return redirect('show')
   else:
       form = AddOrderForm()
   return render(request,'orders/orders_add.html', {'form':form})

def show(request):
    orders = Orders.objects.all()
    return render (request, 'orders/orders_list.html',{'orders':orders})
def authenticate(request):
    pass

def update(request):
    pass

def delete(request):
    pass