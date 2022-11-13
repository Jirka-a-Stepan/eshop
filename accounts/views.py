from django.contrib import messages
from django.contrib.auth import forms, authenticate, login
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.views import LoginView
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView

from accounts.forms import ProfileForm
from accounts.models import User


class RegistrationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('email', 'first_name', 'last_name',)


class RegistrationFormView(CreateView):
    template_name = 'registration.html'
    form_class = RegistrationForm
    success_url = reverse_lazy('login')


class EditProfileView(UpdateView):
    template_name = "edit_profile.html"
    model = User
    form_class = ProfileForm
    success_url = reverse_lazy("products")

def login_request(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            email = form.cleaned_data('email')
            password = form.cleaned_data('password')
            user = authenticate(email=email, password=password)
            if user is not None:
                login(request, user)
                messages.info(request, f"You are now logged in as {email}.")
                return redirect('products')
            else:
                messages.error(request, "Invalid email or password")
        else:
            messages.error(request, "Invalid email or password")
        form = AuthenticationForm()
        return render(request=request, template_name="registration/login.html", context={"form": form})
