from django.shortcuts import render, redirect
from .models import Order, Product


def index(request):
    context = {
        "all_products": Product.objects.all()
    }
    return render(request, "store/index.html", context)


def checkout_process(request):
    for key in ("quantity", "price"):
        request.session[key] = request.POST[key]

    quantity_from_form = int(request.session["quantity"])
    price_from_form = float(request.session["price"])
    total_charge = quantity_from_form * price_from_form
    request.session["total_price"] = total_charge

    if "total_charge_history" not in request.session.keys():
        request.session["total_charge_history"] = 0
    request.session["total_charge_history"] += total_charge

    Order.objects.create(quantity_ordered=quantity_from_form,
                         total_price=total_charge)
    return redirect('/checkout')


def checkout(request):
    return render(request, "store/checkout.html")
