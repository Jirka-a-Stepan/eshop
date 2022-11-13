from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import CreateView, UpdateView, TemplateView
from django.views.generic.edit import FormMixin

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


class LoginView(FormMixin, TemplateView):
    template_name = 'products/products.html'
    form_class = AuthenticationForm

    def post(self, request, *args, **kwargs):
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            messages.success(request, 'Login successfully')
            return redirect('products')
        messages.error(request, 'Wrong credentials')
        return redirect('products')


class LogoutView(View):

    def get(self, request, *args, **kwargs):
        logout(request)
        return redirect('products')
