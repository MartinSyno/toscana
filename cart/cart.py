from decimal import Decimal
from django.conf import settings
from shop.models import Furniture


class Cart(object):

    def __init__(self, request):
        """
        Initialize the cart.
        """
        self.session = request.session
        cart = self.session.get(settings.CART_SESSION_ID)
        if not cart:
            # save an empty cart in the session
            cart = self.session[settings.CART_SESSION_ID] = {}
        self.cart = cart

    def add(self, furniture, quantity=1):
        """
        Add a furniture to the cart or update its quantity.
        """
        furniture_id = str(furniture.id)
        if furniture_id not in self.cart:
            self.cart[furniture_id] = {'quantity': 1, 'price': str(furniture.price)}
        else:
            self.cart[furniture_id]['quantity'] += quantity
        self.save()

    def save(self):
        # mark the session as "modified" to make sure it gets saved
        self.session.modified = True

    def remove(self, furniture):
        """
        Remove a product from the cart.
        """
        furniture_id = str(furniture.id)
        if furniture_id in self.cart:
            del self.cart[furniture_id]
            self.save()

    def get_total_price(self):
        return sum(Decimal(item['price']) * item['quantity'] for item in self.cart.values())

    def clear(self):
        # remove cart from session
        del self.session[settings.CART_SESSION_ID]
        self.save()

    def __iter__(self):
        """
        Iterate over the items in the cart and get the products from the database.
        """
        furniture_ids = self.cart.keys()
        # get the furniture objects and add them to the cart
        furnitures = Furniture.objects.filter(id__in=furniture_ids)
        cart = self.cart.copy()

        for furniture in furnitures:
            cart[str(furniture.id)]['furniture'] = furniture

        for item in cart.values():
            item['price'] = Decimal(item['price'])
            item['total_price'] = item['price'] * item['quantity']
            yield item

    def __len__(self):
        """
        Count all items in the cart.
        """
        return sum(item['quantity'] for item in self.cart.values())