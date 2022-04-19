from rest_framework import serializers

from .models import DeliveryMan


class DeliveryManSerializer(serializers.ModelSerializer):

    class Meta:
        model = DeliveryMan
        fields = 'name'


class DeliveryManDetailSerializer(serializers.ModelSerializer):

    # order_list = OrderListSerializer(many=True)

    class Meta:
        model = DeliveryMan
        fields = '__all__'
