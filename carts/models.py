from django.db import models

from core.models import TimeStampedModel


class Cart(TimeStampedModel):
    user = models.ForeignKey('users.User', on_delete=models.Model)
    product_option = models.ForeignKey('products.ProductOption', on_delete=models.Model)
    quantity = models.IntegerField(default=0)

    class Meta:
        db_table = 'carts'