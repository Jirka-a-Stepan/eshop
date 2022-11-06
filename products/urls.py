import tablet as tablet
from django.contrib import admin

from django.urls import path, include
from products.views import tablet_views, mobile_views, ProductsView




urlpatterns = [
    path('Search/', search.views.search, name='search'),
    path('', ProductsView.as_view(), name="products"),
    path('Mobile/', mobile_views, name='mobile'),
    path('Tablet/', tablet_views, name='tablet'),

]