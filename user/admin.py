from django.contrib import admin

# from main_app.consumer.models import Consumer
# from main_app.delivery_man.models import DeliveryMan
# from main_app.delivery_service.models import DeliveryService
# from main_app.order.models import Order
# from main_app.product.models import Product
from . import models
#
# admin.site.register(Consumer)
# admin.site.register(DeliveryMan)
# admin.site.register(DeliveryService)
# admin.site.register(Order)
# admin.site.register(Product)
admin.site.register(models.User)
