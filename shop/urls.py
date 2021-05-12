from django.urls import path
from .views import *

app_name = "shop"

urlpatterns = [
    path("category/<int:id>/<slug:slug>", category_info_page, name="category_info_page"),
    path("category/<int:category_id>/<slug:category_slug>/furniture/<int:id>/<slug:slug>", furniture_info_page, name="furniture_info_page"),
]