from django.shortcuts import render, get_object_or_404
from .models import *
from main_page.models import SiteSettings
import random


def category_info_page(request, id, slug):
    categories = Category.objects.filter(is_visible=True)
    category = get_object_or_404(Category, id=id, slug=slug, is_visible=True)
    furnitures_of_category = Furniture.objects.filter(category=category.pk).filter(is_visible=True)


    phone = SiteSettings.objects.first().phone
    address = SiteSettings.objects.first().address
    email = SiteSettings.objects.first().email
    facebook_link = SiteSettings.objects.first().facebook_link
    instagram_link = SiteSettings.objects.first().instagram_link

    return render(request, "category_info_page.html", context={
        "categories": categories,
        "category": category,
        "furnitures_of_category": furnitures_of_category,
        "phone": phone,
        "address": address,
        "email": email,
        "facebook_link": facebook_link,
        "instagram_link": instagram_link,
    })


def furniture_info_page(request, id, slug, *args, **kwargs):
    categories = Category.objects.filter(is_visible=True)

    furniture = get_object_or_404(Furniture, id=id, slug=slug, is_visible=True)  # , available=True)

    related_furnitures = [furniture_object for furniture_object in
                          Furniture.objects.filter(category__name=furniture.category.name)]
    random.shuffle(related_furnitures)


    phone = SiteSettings.objects.first().phone
    address = SiteSettings.objects.first().address
    email = SiteSettings.objects.first().email
    facebook_link = SiteSettings.objects.first().facebook_link
    instagram_link = SiteSettings.objects.first().instagram_link
    # cart = Cart(request)
    return render(request, "furniture_info_page.html", context={
        "categories": categories,
        "furniture": furniture,
        "related_furnitures": related_furnitures,
        "phone": phone,
        "address": address,
        "email": email,
        "facebook_link": facebook_link,
        "instagram_link": instagram_link,
    })  # "cart": cart})