from django.shortcuts import render
from shop.models import *
from .models import *
from cart.cart import Cart

categories = Category.objects.filter(is_visible=True)
site_settings = SiteSettings.objects.first()


def main_page(request):
    furnitures = Furniture.objects.filter(is_visible=True)

    discount_furnitures = Furniture.objects.filter(discount__isnull=False)

    # Раздел Последние товары (amount_in_column - сколько отображать в столбце)
    amount_in_column = SiteSettings.objects.first().latest_product_amount_in_column
    latest_furnitures = []
    for i in range(0, len(Furniture.objects.filter(is_visible=True)), amount_in_column):
        latest_furnitures.append(Furniture.objects.filter(is_visible=True).order_by("-created")[i:i+amount_in_column])

    toprated_furnitures = []
    for i in range(0, len(Furniture.objects.filter(is_visible=True)), amount_in_column):
        toprated_furnitures.append(Furniture.objects.filter(is_visible=True).order_by("created")[i:i + amount_in_column])

    banners = Banner.objects.filter(is_visible=True)

    cart = Cart(request)

    return render(request, "main_page_index.html", context={
        "categories": categories,
        "furnitures": furnitures,
        "discount_furnitures": discount_furnitures,
        "banners": banners[:2],
        "latest_furnitures": latest_furnitures,
        "toprated_furnitures": toprated_furnitures,
        "site_settings": site_settings,
        "cart": cart,
    })