from django.db import models


class DeliveryMan(models.Model):
    name = models.TextField()
    orders_list = models.ManyToManyField('order.Order', related_name='orders_list', blank=True)
