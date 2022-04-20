from rest_framework.response import Response
from rest_framework.views import APIView

from .models import User, Order
from .serializers import UserListSerializer, UserDetailSerializer, UserSerializer, OrderSerializer, \
    OrderListSerializer, OrderDetailSerializer


class UserView(APIView):

    def get(self, request):
        products = User.objects
        serializer = UserListSerializer(products, many=True)
        return Response(serializer.data)

    def post(self, request):
        product = UserSerializer(data=request.data)
        if product.is_valid():
            product.save()
        return Response(status=201)


class UserDetailView(APIView):

    def get(self, request, pk):
        product = User.objects.get(id=pk)
        serializer = UserDetailSerializer(product)
        return Response(serializer.data)

    def delete(self, request, pk):
        product = User.objects.get(id=pk)
        product.delete()
        return Response(status=201)

    def put(self, request, pk):
        product = User.objects.get(id=pk)
        serializer = UserSerializer(product, data=request.data)
        if serializer.is_valid():
            serializer.save()
        return Response(UserDetailSerializer(User.objects.get(id=pk)).data)


class OrderView(APIView):

    def get(self, request):
        orders = Order.objects
        serializer = OrderListSerializer(orders, many=True)
        return Response(serializer.data)

    def post(self, request):
        order = OrderSerializer(data=request.data)
        if order.is_valid():
            order.save()
            return Response(status=201)
        else:
            return Response(status=400)


class OrderDetailView(APIView):
    def get(self, request, pk):
        order = Order.objects.get(id=pk)
        serializer = OrderDetailSerializer(order)
        return Response(serializer.data)

    def delete(self, request, pk):
        order = Order.objects.get(id=pk)
        order.delete()
        return Response(status=201)

    def put(self, request, pk):
        order = Order.objects.get(id=pk)
        serializer = OrderSerializer(order, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(OrderDetailSerializer(Order.objects.get(id=pk)).data)
        else:
            return Response(status=400)
