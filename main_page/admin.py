from django.contrib import admin
from .models import *
# Register your models here.

@admin.register(SiteSettings)
class SiteSettingsAdmin(admin.ModelAdmin):
    list_display = ["address", "phone", "email", "latest_product_amount_in_column"]
    list_editable = ["phone", "email", "latest_product_amount_in_column"]
    save_on_top = True
    list_per_page = 20

@admin.register(Banner)
class BannerAdmin(admin.ModelAdmin):
    list_display = ["name", "is_visible"]
    list_filter = ["name", "is_visible"]
    list_editable = ["is_visible"]
    save_on_top = True
    list_per_page = 20