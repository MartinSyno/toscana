from django.shortcuts import render
from cart.cart import Cart
from .forms import OrderCreateForm
from .models import OrderItem
from shop.models import Category
from main_page.models import SiteSettings


# Create your views here.
def order_create(request):
    cart = Cart(request)
    if request.method == "POST":
        # raise ValueError("Fufffff")
        form = OrderCreateForm(request.POST)
        if form.is_valid():
            order = form.save()
            for item in cart:
                OrderItem.objects.create(order=order, furniture=item["furniture"], price=item["price"],
                                         quantity=item["quantity"])

            # clear the cart
            cart.clear()
            return render(request, "checkout_created.html", {"order": order})
    else:
        form = OrderCreateForm()
    # raise ValueError("Огооооо")
    categories = Category.objects.filter(is_visible=True)
    phone = SiteSettings.objects.first().phone
    address = SiteSettings.objects.first().address
    email = SiteSettings.objects.first().email
    facebook_link = SiteSettings.objects.first().facebook_link
    instagram_link = SiteSettings.objects.first().instagram_link
    return render(request, "checkout.html", {
        "cart": cart,
        "form": form,
        "categories": categories,
        "phone": phone,
        "address": address,
        "email": email,
        "facebook_link": facebook_link,
        "instagram_link": instagram_link,
    })
