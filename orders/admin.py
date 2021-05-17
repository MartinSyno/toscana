from django.contrib import admin
from .models import Order, OrderItem

# Register your models here.
class OrderItemInline(admin.TabularInline):
    model = OrderItem
    raw_id_fields = ["furniture"]

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ["code", "first_name", "last_name", "phone_number", "email", "address", "paid", "created", "updated"]
    list_filter = ["paid", "created", "updated"]
    list_editable = ["paid"]
    search_fields = ["code", "first_name", "last_name", "phone_number"]
    save_on_top = True
    inlines = [OrderItemInline]
    readonly_fields = ["code", "first_name", "last_name", "phone_number", "email", "contact_viber", "contact_telegram", "contact_phone", "contact_email", "address"]
    list_per_page = 20