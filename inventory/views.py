from django.shortcuts import render, redirect, get_object_or_404
from .models import Inventory
from django.contrib.auth.decorators import login_required
from .forms import AddInventoryForm
from django.http import HttpResponse
from django_pandas.io import read_frame
import plotly
import plotly.express as px
import json

@login_required
def inventory_list(request):
    inventories = Inventory.objects.all()
    context = {
        "title": "Inventory List",
        "inventories": inventories
    }
    return render(request, "inventory/inventory_list.html", context=context)

@login_required
def per_product_view(request, pk):
    inventory = get_object_or_404(Inventory, pk=pk)
    context = {
        "title": "Inventory Per Product",
        'inventory': inventory
    }

    return render(request,"inventory/per_product.html",context=context)

@login_required
def add_product(request):
    if request.method =="POST":
        add_form = AddInventoryForm( data=request.POST)
        if add_form.is_valid():
            new_inventory = add_form.save(commit=False)
            new_inventory.sales = float(add_form.data['cost_per_item']) * float(add_form.data['quantity_sold'])
            new_inventory.save()
            return redirect("/inventory/")
        else:
            add_form = AddInventoryForm()
        return render(request, "inventory/inventory_add.html", {"form": add_form}, context=context)


@login_required
def dashboard(request):
    inventories = Inventory.objects.all()

    df = read_frame(inventories)

    sales_graph = df.groupby(by="last_sales_date", as_index=False, sort=False)['sales'].sum()
    sales_graph = px.line(sales_graph, x=sales_graph.last_sales_date, y = sales_graph.sales, title="Sales Trend")
    sales_graph = json.dumps(sales_graph, cls=plotly.utils.PlotlyJSONEncoder)

    best_performing_product_df = df.groupby(by="name").sum().sort_values(by="quantity_sold")
    best_performing_product = px.bar(best_performing_product_df, x = best_performing_product_df.index, y = best_performing_product_df.quantity_sold, title="Best Performing Product")
    best_performing_product = json.dumps(best_performing_product, cls=plotly.utils.PlotlyJSONEncoder)

    context = {
        "sales_graph": sales_graph,
        "best_performing_product": best_performing_product,
    }
    return render(request,"erpw/home.html", context=context)
