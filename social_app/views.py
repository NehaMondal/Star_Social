from django.shortcuts import render
from social_app.models import User
from django.urls import reverse_lazy
from . import forms
from django.views.generic import CreateView


# Create your views here.
class Signup(CreateView):
    model = User
    form_class = forms.UserCreateForm
    success_url = reverse_lazy('login')
    template_name = 'social_app/signup.html'
