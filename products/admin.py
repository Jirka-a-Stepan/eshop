from django import forms
from django.contrib import admin

from functions.string_functions import create_alias
from products.models import Product, Producer, OperationSystem, MobileStandard, SimType, SupportedEbookFormat


class ProductAdminForm(forms.ModelForm):
    id = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class': 'vTextField',
                'placeholder': 'Value will generate automaticaly.'
            }),
        label="Idetification number of products",
        required=False,
        disabled=True)
    alias = forms.CharField(
        widget=forms.TextInput(attrs={"class": "vTextField"}),
        required=False)

    # images = None


class ProductAdmin(admin.ModelAdmin):
    form = ProductAdminForm

    list_display = [
        'id',
        'name',
        'product_type',
        'is_published'
    ]
    fieldsets = [
        ('Basic information', {
            'fields': [
                'id',
                'name',
                'alias',
                'producer',
                'product_type',
                'is_published',
                'stock',
                'prize'
            ]
        }),
        ('Additional information', {
            'fields': [
                'description',
                'images',
                'height',
                'width',
                'depth',
                'weight',
                'display_size',
                'internal_memory',
                'battery_capacity',
                'operation_system',
                'mobile_standards',
                'sim_type',
                'touched_display',
                'supported_ebook_formats'
            ]
        })
    ]

    def save_model(self, request, obj, form, change):
        if request.POST.get("alias") == "":
            name = request.POST.get("name")
            obj.alias = create_alias(name)
        super().save_model(request, obj, form, change)


class ProducerAdminForm(forms.ModelForm):
    alias = forms.CharField(
        widget=forms.TextInput(attrs={"class": "vTextField"}),
        required=False)


class ProducerAdmin(admin.ModelAdmin):
    form = ProducerAdminForm

    def save_model(self, request, obj, form, change):
        if request.POST.get("alias") == "":
            name = request.POST.get("name")
            obj.alias = create_alias(name)
        super().save_model(request, obj, form, change)


admin.site.register(Product, ProductAdmin)
admin.site.register(Producer, ProducerAdmin)
admin.site.register(OperationSystem)
admin.site.register(MobileStandard)
admin.site.register(SupportedEbookFormat)
admin.site.register(SimType)
