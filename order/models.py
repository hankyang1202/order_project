from django.contrib.auth.models import User
from django.db import models
from product.models import Product


# Create your models here.


class Order(models.Model):
    order_id = models.BigIntegerField(
        primary_key=True
    )
    customer_id = models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )
    shipping = models.IntegerField(
        default=0
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        null=True,
        blank=True
    )

    @classmethod
    def create(cls, order_id, customer_id, shipping):
        order = cls(
            order_id=order_id,
            customer_id=customer_id,
            shipping=shipping
        )
        return order


class OrderItem(models.Model):
    order = models.ForeignKey(
        Order,
        on_delete=models.CASCADE
    )
    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE
    )
    qty = models.IntegerField(
        default=0
    )

    @classmethod
    def create(cls, order, product, qty):
        order_item = cls(
            order=order,
            product=product,
            qty=qty
        )
        return order_item
