from django.shortcuts import get_object_or_404, redirect, render
from django.views.decorators.http import require_GET

from shop.models import Furniture

from .cart import Cart

from shop.models import Category
# from main_page.models import SiteSettings

# Create your views here.
categories = Category.objects.filter(is_visible=True)
# site_settings = SiteSettings.objects.first()

@require_GET
def cart_add(request, furniture_id):
    cart = Cart(request)
    furniture = get_object_or_404(Furniture, id=furniture_id)
    cart.add(furniture=furniture, quantity=1)
    return redirect("cart:cart_detail")

def cart_remove(request, furniture_id):
    cart = Cart(request)
    furniture = get_object_or_404(Furniture, id=furniture_id)
    cart.remove(furniture)
    return redirect("cart:cart_detail")

def cart_detail(request):
    cart = Cart(request)
    return render(request, "cart_detail.html", {
        "cart": cart,
        "categories": categories,
        # "site_settings": site_settings,
    })
