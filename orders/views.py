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

@login_required
def add(request):
   if request.method == 'POST':
       form = AddOrderForm(request.POST)
       if form.is_valid():
           form.save()
           return redirect('show')
   else:
       form = AddOrderForm()
   return render(request,'orders/orders_add.html', {'form':form})

@login_required
def show(request):
    orders = Orders.objects.all()
    return render (request, 'orders/orders_list.html',{'orders':orders})
@login_required
def authenticate(request, id):
    orders = Orders.objects.get(pk=id)
    orders.is_authenticated = True
    orders.save()
    return redirect('show')

@login_required
def update(request):
    pass

@login_required
def delete(request):
    pass