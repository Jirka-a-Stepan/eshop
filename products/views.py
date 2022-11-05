from django.shortcuts import render
from django.views.generic import TemplateView
from .models import *



def tablet_views(request):
    tablet = Tablet.objects.all()
    context = {'tablet':tablet}
    return render(request, 'products/Tablet.html', context)




def mobile_views(request):
    mobile = Mobile.objects.all()
    context = {'Mobile':Mobile}
    return render(request, 'products/Mobile.html', context)


class ProductsView(TemplateView):
    template_name = 'products/products.html'
