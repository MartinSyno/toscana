from django.shortcuts import render, get_object_or_404
from shop.models import *
from .models import *
import random


def main_page_view(request):
    categories = Category.objects.filter(is_visible=True).order_by("category_ordered")

    for category in categories:
        furnitures_of_category = Furniture.objects.filter(category=category.pk).filter(is_visible=True).order_by("furniture_ordered")
        category.furnitures_of_category = furnitures_of_category

    furnitures = Furniture.objects.filter(is_visible=True).order_by("furniture_ordered")

    # Раздел Последние товары (amount_in_column - сколько отображать в столбце)
    amount_in_column = SiteSettings.objects.first().latest_product_amount_in_column
    latest_furnitures = []
    for i in range(0, len(Furniture.objects.filter(is_visible=True)), amount_in_column):
        latest_furnitures.append(Furniture.objects.filter(is_visible=True).order_by("created")[i:i+amount_in_column])

    toprated_furnitures = []
    for i in range(0, len(Furniture.objects.filter(is_visible=True)), amount_in_column):
        toprated_furnitures.append(Furniture.objects.filter(is_visible=True).order_by("-created")[i:i + amount_in_column])

    phone = SiteSettings.objects.first().phone
    address = SiteSettings.objects.first().address
    email = SiteSettings.objects.first().email
    facebook_link = SiteSettings.objects.first().facebook_link
    instagram_link = SiteSettings.objects.first().instagram_link

    banners = Banner.objects.filter(is_visible=True)

    return render(request, "main_page_index.html", context={
        "categories": categories,
        "furnitures": furnitures,
        "banners": banners[0:2],
        "latest_furnitures": latest_furnitures,
        "toprated_furnitures": toprated_furnitures,
        "phone": phone,
        "address": address,
        "email": email,
        "facebook_link": facebook_link,
        "instagram_link": instagram_link,
    })


def category_info_page(request, id, slug):
    categories = Category.objects.filter(is_visible=True).order_by("category_ordered")
    category = get_object_or_404(Category, id=id, slug=slug, is_visible=True)
    furnitures_of_category = Furniture.objects.filter(category=category.pk).filter(is_visible=True).order_by(
        "furniture_ordered")

    return render(request, "category_info_page.html", context={
        "categories": categories,
        "category": category,
        "furnitures_of_category": furnitures_of_category,
    })


def furniture_info_page(request, id, slug):
    categories = Category.objects.filter(is_visible=True).order_by("category_ordered")
    
    furniture = get_object_or_404(Furniture, id=id, slug=slug, is_visible=True)#, available=True)
    
    related_furnitures = [furniture_object for furniture_object in Furniture.objects.filter(category__name=furniture.category.name)]
    random.shuffle(related_furnitures)
    # cart = Cart(request)
    return render(request, "furniture_info_page.html", context={
        "categories": categories,
        "furniture": furniture,
        "related_furnitures": related_furnitures,
    })#"cart": cart})