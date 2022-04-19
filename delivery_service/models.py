from django.db import models


class DeliveryService(models.Model):
    name = models.TextField()
    workers_list = models.ManyToManyField('delivery_man.DeliveryMan', related_name='workers_list', blank=True)
