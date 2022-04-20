from django.db import models


class DeliveryService(models.Model):
    name = models.TextField()
    workers_list = models.ManyToManyField('DeliveryMan', related_name='workers_list', blank=True)


class DeliveryMan(models.Model):
    name = models.TextField()
    orders_list = models.ManyToManyField('user.Order', related_name='orders_list', blank=True)
