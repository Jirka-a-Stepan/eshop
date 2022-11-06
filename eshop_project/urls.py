
The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
import django
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.auth import views
from django.urls import path, include
from django.urls import path, include
from products.views import tablet_views, mobile_views, ProductsView


import accounts.views
import products.views
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include("django.contrib.auth.urls")),
    path('accounts/edit_profile/<pk>', accounts.views.EditProfileView.as_view(), name='edit_profile'),
    path('accounts/registration/', accounts.views.RegistrationFormView.as_view(), name='registration_form'),
    path('', products.views.ProductsView.as_view(), name='products'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
