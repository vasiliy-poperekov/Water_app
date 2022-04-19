from django.db import models


class User(models.Model):
    name = models.TextField()
    phone_number = models.TextField()
    orders = models.ManyToManyField('order.Order', related_name='orders', blank=True)
