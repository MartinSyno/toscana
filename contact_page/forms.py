from django import forms
from .models import Message

class FormMessage(forms.ModelForm):
    user_name = forms.CharField(max_length=40,
                                widget=forms.TextInput(attrs={"type": "text", "placeholder": "Ім\'я"}))#, "required": "required"}))
    user_email = forms.EmailField(
        widget=forms.EmailInput(attrs={"type": "email", "placeholder": "Електронна пошта"}))#, "required": "required"}))
    user_message = forms.CharField(max_length=500,
                                   widget=forms.Textarea(
                                       attrs={"placeholder": "Повідомлення"}))#, "required": "required"}))

    class Meta:
        model = Message
        fields = ("user_name", "user_email", "user_message")
