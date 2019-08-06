from django.contrib import admin

# Register your models here.
# Register your models here.
from .models import Product


# Register your models here.
class ProductAdmin(admin.ModelAdmin):
    pass


admin.site.register(Product, ProductAdmin)
