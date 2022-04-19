from django.db import models


class Order(models.Model):
    product = models.ForeignKey('product.Product', on_delete=models.CASCADE, related_name='count_of_products', null=True)
    user = models.ForeignKey('user.User', on_delete=models.CASCADE, related_name='user_id')
    count_of_products = models.IntegerField()
    address = models.TextField()
