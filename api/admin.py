from django.contrib import admin
from .models import Product, Order, OrderItem, Organization, Sushiproducts, AppVersion

admin.site.register(Product)
admin.site.register(Sushiproducts)
admin.site.register(Order)
admin.site.register(OrderItem)
admin.site.register(Organization)
admin.site.register(AppVersion)