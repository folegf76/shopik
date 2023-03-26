from django import forms
from django.contrib.auth import get_user_model, authenticate


User = get_user_model()


class Search(forms.Form):
    sear = forms.CharField(widget=forms.TextInput(attrs={'type': "text", 'placeholder': "Search product."}))

