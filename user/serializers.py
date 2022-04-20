from rest_framework import serializers

from .models import User, Order
from factory.serializers import ProductListSerializer


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'


class OrderDetailSerializer(serializers.ModelSerializer):
    product = ProductListSerializer()
    user = UserSerializer()

    class Meta:
        model = Order
        fields = '__all__'


class UserListSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'name')


class UserDetailSerializer(serializers.ModelSerializer):
    orders = OrderDetailSerializer(many=True)

    class Meta:
        model = User
        fields = '__all__'


class OrderListSerializer(serializers.ModelSerializer):
    product = ProductListSerializer()

    class Meta:
        model = Order
        fields = ('id', 'product', 'count_of_products')


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = '__all__'
