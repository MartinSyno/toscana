from django.db import models
from shop.models import Furniture
import random

# Create your models here.


class Order(models.Model):

    def random_number(*args, **kwargs):
        return random.randint(100_000_000, 999_999_999)

    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    phone_number = models.CharField(max_length=13)
    email = models.EmailField()
    address = models.CharField(max_length=250)
    contact_viber = models.BooleanField(default=False)
    contact_telegram = models.BooleanField(default=False)
    contact_phone = models.BooleanField(default=False)
    contact_email = models.BooleanField(default=False)
    code = models.CharField(max_length=20, default=random_number)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    paid = models.BooleanField(default=False)

    class Meta():
        ordering = ("-created",)

    def __str__(self):
        return f"Order {self.id}"

    def get_total_cost(self):
        return sum(item.get_cost() for item in self.item.all())


class OrderItem(models.Model):
    order = models.ForeignKey(Order, related_name="items", on_delete=models.CASCADE)
    furniture = models.ForeignKey(Furniture, related_name="order_items", on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return f"{self.id}"

    def get_cost(self):
        return self.price * self.quantity
