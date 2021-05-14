from django import forms

from .models import Order

class OrderCreateForm(forms.ModelForm):
    first_name = forms.CharField(max_length=50, widget=forms.TextInput(attrs={"type": "text", "placeholder": "Ім'я"}))
    last_name = forms.CharField(max_length=50, widget=forms.TextInput(attrs={"type": "text", "placeholder": "Прізвище"}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={"type": "email", "placeholder": "email@example.com"}))
    address = forms.CharField(max_length=250, widget=forms.TextInput(attrs={"type": "text", "placeholder": "Вулиця, будинок"}))
    city = forms.CharField(max_length=100, widget=forms.TextInput(attrs={"type": "text", "placeholder": "Місто"}))

    class Meta:
        model = Order
        fields = ('first_name', 'last_name', 'email', 'address', 'city')
