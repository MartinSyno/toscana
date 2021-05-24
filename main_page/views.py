from django.shortcuts import render
from shop.models import Category, Furniture
from .models import *
from cart.cart import Cart
import random

categories = Category.objects.filter(is_visible=True)
# site_settings = SiteSettings.objects.first()


def main_page(request):
    furnitures = Furniture.objects.filter(is_visible=True)

    discount_furnitures = Furniture.objects.filter(discount__isnull=False)

    new_furnitures = []
    for category in categories:
        new_furnitures.append(Furniture.objects.filter(is_visible=True, category=category).order_by("-created")[:4])


    # Раздел Последние товары (amount_in_column - сколько отображать в столбце)
    amount_in_column = SiteSettings.objects.first().latest_product_amount_in_column
    latest_furnitures = []
    for i in range(0, len(furnitures), amount_in_column):
        latest_furnitures.append(Furniture.objects.filter(is_visible=True).order_by("-created")[i:i+amount_in_column])
        if len(latest_furnitures) >= 5:
            break

    def add_random_furnitures(f_list):
        random_furnitures_list = list(furnitures)
        random.shuffle(random_furnitures_list)
        random_furnitures_list = random_furnitures_list[: 5 * amount_in_column]
        for i in range(0, len(random_furnitures_list), amount_in_column):
            furnitures_group = random_furnitures_list[i: i + amount_in_column]
            f_list.append(furnitures_group)
            if len(f_list) >= 5:
                break
    random_furnitures = []
    add_random_furnitures(random_furnitures)

    banners = Banner.objects.filter(is_visible=True)

    cart = Cart(request)

    return render(request, "main_page_index.html", context={
        "categories": categories,
        "furnitures": furnitures,
        "new_furnitures": new_furnitures,
        "discount_furnitures": discount_furnitures,
        "banners": banners[:2],
        "latest_furnitures": latest_furnitures,
        "random_furnitures": random_furnitures,
        # "site_settings": site_settings,
        "cart": cart,
    })