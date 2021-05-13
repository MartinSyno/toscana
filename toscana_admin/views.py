from django.shortcuts import render, redirect
from contact_page.models import Message
from main_page.models import SiteSettings
from shop.models import Category

from django.contrib.auth.decorators import login_required, user_passes_test

# Create your views here.

def is_admin(user):
    return user.is_staff

@login_required(login_url="/admin/login/")
@user_passes_test(is_admin)
def messages_list(request):
    messages = Message.objects.filter(is_processed=False)

    categories = Category.objects.filter(is_visible=True)
    phone = SiteSettings.objects.first().phone
    address = SiteSettings.objects.first().address
    email = SiteSettings.objects.first().email
    facebook_link = SiteSettings.objects.first().facebook_link
    instagram_link = SiteSettings.objects.first().instagram_link
    return render(request, "messages_list.html", context={
        "messages": messages,
        "categories": categories,
        "phone": phone,
        "address": address,
        "email": email,
        "facebook_link": facebook_link,
        "instagram_link": instagram_link,
    })

@login_required(login_url="/admin/login/")
@user_passes_test(is_admin)
def message_update(request, pk):
    Message.objects.filter(pk=pk).update(is_processed=True)
    return redirect("toscana_admin:messages_list")