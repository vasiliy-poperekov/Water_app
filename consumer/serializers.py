from rest_framework import serializers

from .models import Consumer
from product.serializers import ProductListSerializer


class ConsumerSerializer(serializers.ModelSerializer):

    class Meta:
        model = Consumer
        fields = '__all__'


class ConsumerListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Consumer
        fields = ("id", "name")


class ConsumerDetailSerializer(serializers.ModelSerializer):

    products = ProductListSerializer(many=True)

    class Meta:
        model = Consumer
        fields = '__all__'
