from django.shortcuts import render, redirect
from shop.models import Category
from main_page.models import SiteSettings
from .forms import FormMessage
from cart.cart import Cart

# Create your views here.

categories = Category.objects.filter(is_visible=True)
phone = SiteSettings.objects.first().phone
address = SiteSettings.objects.first().address
email = SiteSettings.objects.first().email
facebook_link = SiteSettings.objects.first().facebook_link
instagram_link = SiteSettings.objects.first().instagram_link


def contact_page(request):

    if request.method == "POST":
        form = FormMessage(request.POST)
        if form.is_valid():
            form.save()
            return redirect("main_page:contact_page")

    working_hours = SiteSettings.objects.first().working_hours

    form = FormMessage()

    cart = Cart(request)

    return render(request, "contact_page.html", context={
        "categories":categories,
        "phone": phone,
        "address": address,
        "email": email,
        "facebook_link": facebook_link,
        "instagram_link": instagram_link,
        "working_hours": working_hours,
        "form": form,
        "cart": cart,
    })
