from django.shortcuts import render, redirect, get_object_or_404
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
           return redirect('orders:show')
   else:
       form = AddOrderForm()
   return render(request,'orders/orders_add.html', {'form':form})

@login_required
def show(request):
    orders = Orders.objects.all()
    return render (request, 'orders/orders_list.html',{'orders':orders})

#admin approval
def approval(request):
    order_list =  Orders.objects.all()
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

            #for delete-------------------------------------------------

            id_deleteorder_true = request.POST.getlist('boxes2')

            for x in id_deleteorder_true:
                Orders.objects.filter(pk=int(x)).delete()

            id_deleteset_false = set(orders_all_ids) - set(id_deleteorder_true)
            id_deletelist_false = list(id_deleteset_false)

            #for y in id_deletelist_false:
                #Orders.objects.filter(pk=int(y)).update(approved=False)

            return redirect('orders:orders')
        else:
            return render(request, 'orders/orders_approval.html',{"order_list":order_list})
    else:
        messages.info(request, ("Error, You aren't authorized to view this page!"))
        return redirect('orders')
    return render(request, 'orders/orders_approval.html')


