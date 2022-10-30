from django.contrib import admin

from accounts.models import User


class UserAdmin(admin.ModelAdmin):
    list_display = ['email', 'first_name', 'last_name']
    fieldsets = [
        ('Personal information', {
            'fields': [
                'avatar',
                'first_name',
                'last_name'
            ]
        }),
        ('Contact information', {
            'fields': [
                'email',
                'country',
                'street',
                'city',
                'zip_code',
                'phone',
            ]
        }),
        ('Communication channel', {
            'fields': [
                'communication_channel',
            ],
            'description': 'Please insert contact phone, email or address here.'
        }),
        ('System information', {
            'fields': [
                'last_login',
                'date_joined',
                'is_superuser',
                'is_staff',
                'is_active',
            ]
        }),
    ]
    readonly_fields = [
        'last_login',
        'date_joined',
    ]


admin.site.register(User, UserAdmin)
