from django.shortcuts import render, redirect
from cart.cart import Cart
from .forms import OrderCreateForm
from .models import OrderItem
from shop.models import Category
from main_page.models import SiteSettings


# Create your views here.
categories = Category.objects.filter(is_visible=True)
site_settings = SiteSettings.objects.first()

def order_create(request):
    cart = Cart(request)
    if request.method == "POST":
        if len(cart) == 0:
            return redirect("main_page:main_page_view")
        form = OrderCreateForm(request.POST)
        if form.is_valid():
            order = form.save()
            for item in cart:
                OrderItem.objects.create(order=order, furniture=item["furniture"], price=item["price"],
                                         quantity=item["quantity"])
            cart.clear()
            return render(request, "checkout_created.html", {
                "order": order,
                "categories": categories,
                "site_settings": site_settings,
            })
    else:
        form = OrderCreateForm()
    return render(request, "checkout.html", {
        "cart": cart,
        "form": form,
        "categories": categories,
        "site_settings": site_settings,
    })
