from django.contrib.auth import forms
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView

from accounts.models import User


class RegistrationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('email', 'first_name', 'last_name', )


class RegistrationFormView(CreateView):
    template_name = 'accounts/registration.html'
    form_class = RegistrationForm
    success_url = reverse_lazy('registration_form')
