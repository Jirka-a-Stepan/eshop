from django.contrib import admin

from products.models import Product, Producer, OperationSystem, MobileStandard, SimType, SupportedEbookFormat

admin.site.register(Product)
admin.site.register(Producer)
admin.site.register(OperationSystem)
admin.site.register(MobileStandard)
admin.site.register(SupportedEbookFormat)
admin.site.register(SimType)
