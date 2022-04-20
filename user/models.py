from django.db import models


class User(models.Model):
    name = models.TextField()
    phone_number = models.TextField()
    orders = models.ManyToManyField('Order', related_name='orders', blank=True)


class Order(models.Model):
    product = models.ForeignKey('factory.Product', on_delete=models.CASCADE, related_name='count_of_products',
                                null=True)
    user = models.ForeignKey('User', on_delete=models.CASCADE, related_name='user_id')
    count_of_products = models.IntegerField()
    address = models.TextField()
