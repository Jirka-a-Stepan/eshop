
from django.contrib import admin
from django.contrib.auth import views
from django.urls import path, include
from django.urls import path, include
from products.views import tablet_views, mobile_views, ProductsView



urlpatterns = [
    path("admin/", admin.site.urls),

    path('', ProductsView.as_view(), name="products"),
    path('Mobile/', mobile_views, name='mobile'),
    path('Tablet/', tablet_views, name='tablet'),
]