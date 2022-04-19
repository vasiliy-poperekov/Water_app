from django.db import models


class Product(models.Model):
    name = models.TextField()
    volume = models.FloatField()
    consist = models.TextField()
    consumer = models.ForeignKey('consumer.Consumer', on_delete=models.CASCADE, related_name='consumer', blank=True,
                                 null=True)
