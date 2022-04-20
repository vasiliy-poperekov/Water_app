from rest_framework import serializers

from .models import Consumer, Product


class ConsumerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Consumer
        fields = '__all__'


class ConsumerListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Consumer
        fields = ('id', 'name')


class ProductListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ('id', 'name', 'volume')


class ConsumerDetailSerializer(serializers.ModelSerializer):
    products = ProductListSerializer(many=True)

    class Meta:
        model = Consumer
        fields = '__all__'


class ProductDetailSerializer(serializers.ModelSerializer):
    consumer = ConsumerListSerializer()

    class Meta:
        model = Product
        fields = '__all__'


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'

