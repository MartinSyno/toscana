from django.shortcuts import render, redirect
from shop.models import Category
from main_page.models import SiteSettings
from .forms import FormMessage
from cart.cart import Cart

# Create your views here.

categories = Category.objects.filter(is_visible=True)
site_settings = SiteSettings.objects.first()


def contact_page(request):

    if request.method == "POST":
        form = FormMessage(request.POST)
        if form.is_valid():
            form.save()
            return redirect("main_page:contact_page")

    form = FormMessage()
    cart = Cart(request)

    return render(request, "contact_page.html", context={
        "categories": categories,
        "site_settings": site_settings,
        "form": form,
        "cart": cart,
    })
