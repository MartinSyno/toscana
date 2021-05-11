from django.urls import path
from .views import *

app_name = "main_page"

urlpatterns = [
    path("", main_page_view, name="main_page_view"),
    path("shop/category/<int:id>/<slug:slug>", category_info_page, name="category_info_page"),
    path("shop/furniture/<int:id>/<slug:slug>", furniture_info_page, name="furniture_info_page"),
]