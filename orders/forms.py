from django import forms

from .models import Order


class OrderCreateForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['first_name', 'last_name', 'address_street', 'address_apartment', 'address_city', 'postal_code',
                  'email', 'phone']

    first_name = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'type': "text"}))
    last_name = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'type': "text"}))
    address_street = forms.CharField(max_length=50, widget=forms.TextInput(attrs={
                    'placeholder': "Введіть назву вулиці і номер дома", 'type': "text"}))
    address_apartment = forms.CharField(max_length=50, widget=forms.TextInput(attrs={
                    'placeholder': "Введіть номер квартири", 'type': "text"}))
    address_city = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'type': "text"}))
    postal_code = forms.CharField(max_length=20, widget=forms.TextInput(attrs={'type': "text"}))
    phone = forms.CharField(max_length=30, widget=forms.TextInput(attrs={'type': "text"}))
    email = forms.EmailField(widget=forms.TextInput(attrs={'type': "text"}))
