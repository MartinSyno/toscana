from django.shortcuts import render
from shop.models import Category
from main_page.models import SiteSettings

# Create your views here.
def contact_page(request):
    categories = Category.objects.filter(is_visible=True)
    phone = SiteSettings.objects.first().phone
    address = SiteSettings.objects.first().address
    email = SiteSettings.objects.first().email
    facebook_link = SiteSettings.objects.first().facebook_link
    instagram_link = SiteSettings.objects.first().instagram_link
    return render(request, "contact_page.html", context={
        "categories":categories,
        "phone": phone,
        "address": address,
        "email": email,
        "facebook_link": facebook_link,
        "instagram_link": instagram_link,
    })
