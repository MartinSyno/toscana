from django.shortcuts import render, get_object_or_404
from .models import *
# from main_page.models import SiteSettings
from cart.cart import Cart
from django.core.paginator import Paginator
import random

categories = Category.objects.filter(is_visible=True)
# site_settings = SiteSettings.objects.first()

def category_info_page(request, id, slug):
    category = get_object_or_404(Category, id=id, slug=slug, is_visible=True)
    furnitures_of_category = Furniture.objects.filter(category=category.pk).filter(is_visible=True)

    paginator = Paginator(furnitures_of_category, 8)
    page = request.GET.get("page")
    furnitures_of_category = paginator.get_page(page)

    cart = Cart(request)

    return render(request, "category_info_page.html", context={
        "categories": categories,
        "category": category,
        "furnitures_of_category": furnitures_of_category,
        # "site_settings": site_settings,
        "cart": cart,
    })

def furniture_info_page(request, id, slug, *args, **kwargs):
    furniture = get_object_or_404(Furniture, id=id, slug=slug, is_visible=True)  # , available=True)

    related_furnitures = [furniture_object for furniture_object in
                          Furniture.objects.filter(category__name=furniture.category.name)]
    random.shuffle(related_furnitures)

    cart = Cart(request)

    return render(request, "furniture_info_page.html", context={
        "categories": categories,
        "furniture": furniture,
        "related_furnitures": related_furnitures[:4],
        # "site_settings": site_settings,
        "cart": cart,
    })