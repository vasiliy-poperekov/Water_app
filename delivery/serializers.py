from rest_framework import serializers

from .models import DeliveryService, DeliveryMan
from user.serializers import OrderListSerializer


class DeliveryServiceListSerializer(serializers.ModelSerializer):
    class Meta:
        model = DeliveryService
        fields = ('id', 'name')


class DeliveryServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = DeliveryService
        fields = '__all_'


class DeliveryManListSerializer(serializers.ModelSerializer):
    class Meta:
        model = DeliveryMan
        fields = ('id', 'name')


class DeliveryServiceDetailSerializer(serializers.ModelSerializer):
    workers_list = DeliveryManListSerializer(many=True)

    class Meta:
        model = DeliveryService
        fields = '__all__'


class DeliveryManDetailSerializer(serializers.ModelSerializer):
    orders_list = OrderListSerializer(many=True)

    class Meta:
        model = DeliveryMan
        fields = '__all__'


class DeliveryManSerializer(serializers.ModelSerializer):
    class Meta:
        model = DeliveryMan
        fields = '__all__'
