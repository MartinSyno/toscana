from django import forms

from .models import Order

class OrderCreateForm(forms.ModelForm):
    first_name = forms.CharField(max_length=50, widget=forms.TextInput(attrs={"type": "text", "placeholder": "Ім\'я"}))
    last_name = forms.CharField(max_length=50, widget=forms.TextInput(attrs={"type": "text", "placeholder": "Прізвище"}))
    phone_number = forms.CharField(max_length=13, widget=forms.TextInput(attrs={"type": "text", "placeholder": "+38 012 345 6789"}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={"type": "email", "placeholder": "email@example.com"}))
    contact_viber = forms.BooleanField(initial=False, required=False, widget=forms.CheckboxInput(attrs={"type": "checkbox"}))
    contact_telegram = forms.BooleanField(initial=False, required=False, widget=forms.CheckboxInput(attrs={"type": "checkbox"}))
    contact_phone = forms.BooleanField(initial=True, required=False, widget=forms.CheckboxInput(attrs={"type": "checkbox"}))
    contact_email = forms.BooleanField(initial=False, required=False, widget=forms.CheckboxInput(attrs={"type": "checkbox"}))
    address = forms.CharField(max_length=250, widget=forms.TextInput(attrs={"type": "text", "placeholder": "Місто\село, вулиця, будинок"}))

    class Meta:
        model = Order
        fields = ("first_name", "last_name", "email", "contact_viber", "contact_telegram", "contact_phone", "contact_email", "phone_number", "address")
