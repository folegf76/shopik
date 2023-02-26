from django.shortcuts import render
from .forms import RegistrationForm

# Create your views here.
def login_view(request):
    pass

def logout_view(request):
    pass

def registration_view(request):
    form = RegistrationForm(request.POST or None)
    if form.is_valid():
