from django.db import models


class Consumer(models.Model):
    name = models.TextField()
    products = models.ManyToManyField('product.Product', related_name='products', blank=True)
    well_info = models.TextField()
