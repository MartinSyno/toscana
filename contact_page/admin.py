from django.contrib import admin
from .models import Message
# Register your models here.
@admin.register(Message)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ["user_name", "user_email", "pub_date", "is_processed"]
    list_filter = ["pub_date", "is_processed"]
    list_editable = ["is_processed"]
    save_on_top = True
    list_per_page = 20
    readonly_fields = ["user_name", "user_email", "user_message", "pub_date"]