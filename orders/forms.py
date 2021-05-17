from django import forms

from .models import Order

class OrderCreateForm(forms.ModelForm):
    first_name = forms.CharField(max_length=50, widget=forms.TextInput(attrs={"type": "text", "placeholder": "Ім\'я"}))
    last_name = forms.CharField(max_length=50, widget=forms.TextInput(attrs={"type": "text", "placeholder": "Прізвище"}))
    phone_number = forms.CharField(max_length=13, widget=forms.TextInput(attrs={"type": "text", "placeholder": "+38 012 345 6789"}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={"type": "email", "placeholder": "email@example.com"}))
    address = forms.CharField(max_length=250, widget=forms.TextInput(attrs={"type": "text", "placeholder": "Місто\село, вулиця, будинок"}))

    class Meta:
        model = Order
        fields = ("first_name", "last_name", "email", "phone_number", "address")
