from django.shortcuts import render, redirect
from contact_page.models import Message
from main_page.models import SiteSettings
from shop.models import Category

from django.contrib.auth.decorators import login_required, user_passes_test
from django.core.paginator import Paginator
from cart.cart import Cart

# Create your views here.
categories = Category.objects.filter(is_visible=True)
site_settings = SiteSettings.objects.first()


def is_admin(user):
    return user.is_staff

@login_required(login_url="/admin/login/")
@user_passes_test(is_admin)
def messages_list(request):
    messages = Message.objects.filter(is_processed=False)

    paginator = Paginator(messages, 5)
    page = request.GET.get("page")
    messages = paginator.get_page(page)

    cart = Cart(request)

    return render(request, "messages_list.html", context={
        "messages": messages,
        "categories": categories,
        "site_settings": site_settings,
        "cart": cart,
    })

@login_required(login_url="/admin/login/")
@user_passes_test(is_admin)
def message_update(request, pk):
    Message.objects.filter(pk=pk).update(is_processed=True)
    return redirect("toscana_admin:messages_list")