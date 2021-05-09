from django.shortcuts import render
from shop.models import *
from .models import *

# Create your views here.
def main_page_view(request):
    categories = Category.objects.filter(is_visible=True).order_by("category_ordered")

    for category in categories:
        furnitures_of_category = Furniture.objects.filter(category=category.pk).filter(is_visible=True).order_by("furniture_ordered")
        category.furnitures_of_category = furnitures_of_category

    furnitures = Furniture.objects.filter(is_visible=True).order_by("furniture_ordered")


    #Раздел Последние товары (amount_in_column - сколько отображать в столбце)
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