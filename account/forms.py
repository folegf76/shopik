from django import forms
from django.contrib.auth import get_user_model

User = get_user_model()

class RegistrationForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('username', )

    username = forms.CharField(widget=forms.TextInput(attrs={'type': "text"}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'type': "password"}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'type': "password2"}))

    def clean_password2(self):
        if self.cleaned_data['password'] == self.cleaned_data['password2']:
            return self.cleaned_data['password2']
        raise forms.ValidationError('Паролі не співпадають')
