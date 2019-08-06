from django.db import models

# Create your models here.


class Product(models.Model):
    product_name = models.CharField(
        max_length=256,
    )
    unit_price = models.IntegerField(
        default=0
    )

    @classmethod
    def create(cls, product_name, unit_price):
        order = cls(
            product_name=product_name,
            unit_price=unit_price
        )
        return order
