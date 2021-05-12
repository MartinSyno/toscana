from django.urls import path
from .views import *
from contact_page.views import *

app_name = "main_page"

urlpatterns = [
    path("", main_page, name="main_page_view"),
    path("contact/", contact_page, name="contact_page"),
]