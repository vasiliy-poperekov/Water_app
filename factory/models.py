from django.db import models


class Consumer(models.Model):
    name = models.TextField()
    products = models.ManyToManyField('Product', related_name='products', blank=True)
    well_info = models.TextField()


class Product(models.Model):
    name = models.TextField()
    volume = models.FloatField()
    consist = models.TextField()
    consumer = models.ForeignKey('Consumer', on_delete=models.CASCADE, related_name='consumer', blank=True,
                                 null=True)
