from django.shortcuts import render
from cart.cart import Cart
from .forms import OrderCreateForm
from .models import OrderItem

# Create your views here.
def order_create(request):
    cart = Cart(request)
    if request.method == 'POST':
        form = OrderCreateForm(request.POST)
        if form.is_valid():
            order = form.save()
            for item in cart:
                OrderItem.objects.create(order=order, furniture=item['furniture'], price=item['price'],
                                         quantity=item['quantity'])

            # clear the cart
            cart.clear()
            return render(request, 'checkout_created.html', {'order': order})
    else:
        form = OrderCreateForm()
    return render(request, 'checkout.html', {'cart': cart, 'form': form})