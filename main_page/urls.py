from django.urls import path
from .views import *

app_name = "main_page"

urlpatterns = [
    path("", main_page_view, name="main_page_view"),
]