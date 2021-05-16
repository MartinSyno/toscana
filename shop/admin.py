from django.contrib import admin
from .models import *

# Register your models here.

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ["name", "slug", "category_ordered", "is_visible"]#["title", "slug", "photo", "dish_order", "is_visible", "price", "available", "desc", "category", "created", "updated"]
    list_filter = ["name", "is_visible"]
    list_editable = ["category_ordered", "is_visible"]
    search_fields = ["name"]
    save_on_top = True
    prepopulated_fields = {"slug": ("name",)}

class FurniturePhotosInline(admin.StackedInline):
    model = Photos

@admin.register(Furniture)
class FurnitureAdmin(admin.ModelAdmin):
    list_display = ["name", "slug", "is_visible", "price", "available", "furniture_ordered", "category", "updated"]#["title", "slug", "photo", "dish_order", "is_visible", "price", "available", "desc", "category", "created", "updated"]
    list_filter = ["is_visible", "available", "created", "updated", "category"]
    list_editable = ["is_visible", "price", "available", "furniture_ordered", "category"]
    search_fields = ["name"]
    save_on_top = True
    prepopulated_fields = {"slug": ("name",)}
    inlines = [FurniturePhotosInline]
