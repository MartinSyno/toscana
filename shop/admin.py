from django.contrib import admin
from .models import *

# Register your models here.

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ["name", "slug", "category_ordered", "is_visible"]#["title", "slug", "photo", "dish_order", "is_visible", "price", "available", "desc", "category", "created", "updated"]
    list_filter = ["name", "is_visible"]
    list_editable = ["category_ordered", "is_visible"]
    prepopulated_fields = {"slug": ("name",)}

@admin.register(Furniture)
class FurnitureAdmin(admin.ModelAdmin):
    list_display = ["name", "slug", "price", "available", "furniture_ordered", "category", "updated"]#["title", "slug", "photo", "dish_order", "is_visible", "price", "available", "desc", "category", "created", "updated"]
    list_filter = ["available", "is_visible", "created", "updated"]
    list_editable = ["price", "available", "furniture_ordered", "category"]
    prepopulated_fields = {"slug": ("name",)}
