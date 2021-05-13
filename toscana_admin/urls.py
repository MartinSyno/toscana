from django.urls import path
from .views import *

app_name = "toscana_admin"

urlpatterns = [
    path("messages/", messages_list, name="messages_list"),
    path("messages/update/<int:pk>", message_update, name="message_update"),
]