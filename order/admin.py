from django.contrib import admin

# Register your models here.
from .models import Order, OrderItem


# Register your models here.
class OrderAdmin(admin.ModelAdmin):
    pass


class OrderItemAdmin(admin.ModelAdmin):
    pass


admin.site.register(Order, OrderAdmin)
admin.site.register(OrderItem, OrderItemAdmin)
