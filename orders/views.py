from django.shortcuts import render, redirect
from .models import Orders
from .forms import AddOrderForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages


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

#admin approval
def approval(request):
    order_list =  Orders.objects.all().order_by('-order_date')
    orders_all = Orders.objects.all()
    orders_all_ids = []

    for i in range(0, len(orders_all), 1):
        orders_all_ids.append(str(orders_all[i].id))

    if request.user.is_superuser:
        if request.method == "POST":
            id_order_true = request.POST.getlist('boxes')

            for x in id_order_true:
                Orders.objects.filter(pk=int(x)).update(approved=True)

            id_set_false = set(orders_all_ids) - set(id_order_true)
            id_list_false = list(id_set_false)

            for y in id_list_false:
                Orders.objects.filter(pk=int(y)).update(approved=False)

            return redirect('orders')
        else:
            return render(request, 'orders/orders_approval.html',{"order_list":order_list})
    else:
        messages.info(request, ("Error, You aren't authorized to view this page!"))
        return redirect('orders')
    return render(request, 'orders/orders_approval.html')