from django.db import models

# Create your models here.


class Product(models.Model):
    product_name = models.CharField(
        max_length=256,
    )
    unit_price = models.IntegerField(
        default=0
    )
