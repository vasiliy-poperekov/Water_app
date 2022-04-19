from rest_framework import serializers

from .models import DeliveryService


class DeliveryServiceSerializer(serializers.ModelSerializer):

    class Meta:
        model = DeliveryService
        fields = 'name'


class DeliveryManDetailSerializer(serializers.ModelSerializer):

    # workers_list = OrderListSerializer(many=True)

    class Meta:
        model = DeliveryService
        fields = '__all__'
