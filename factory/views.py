from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Consumer, Product
from .serializers import ConsumerListSerializer, ConsumerDetailSerializer, ConsumerSerializer, ProductSerializer, \
    ProductListSerializer, ProductDetailSerializer


class ConsumerView(APIView):

    def get(self, request):
        consumers = Consumer.objects
        serializer = ConsumerListSerializer(consumers, many=True)
        return Response(serializer.data)

    def post(self, request):
        consumer = ConsumerSerializer(data=request.data)
        if consumer.is_valid():
            consumer.save()
            return Response(status=201)
        else:
            return Response(status=400)


class ConsumerDetailView(APIView):

    def get(self, request, pk):
        consumer = Consumer.objects.get(id=pk)
        serializer = ConsumerDetailSerializer(consumer)
        return Response(serializer.data)

    def delete(self, request, pk):
        consumer = Consumer.objects.get(id=pk)
        consumer.delete()
        return Response(status=201)

    def put(self, request, pk):
        consumer = Consumer.objects.get(id=pk)
        serializer = ConsumerSerializer(consumer, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(ConsumerDetailSerializer(Consumer.objects.get(id=pk)).data)
        else:
            return Response(status=400)


class ProductListView(APIView):

    def get(self, request):
        products = Product.objects
        serializer = ProductListSerializer(products, many=True)
        return Response(serializer.data)

    def post(self, request):
        product = ProductSerializer(data=request.data)
        if product.is_valid():
            product.save()
        return Response(status=201)


class ProductDetailView(APIView):

    def get(self, request, pk):
        product = Product.objects.get(id=pk)
        serializer = ProductDetailSerializer(product)
        return Response(serializer.data)

    def delete(self, request, pk):
        product = Product.objects.get(id=pk)
        product.delete()
        return Response(status=201)

    def put(self, request, pk):
        product = Product.objects.get(id=pk)
        serializer = ProductSerializer(product, data=request.data)
        if serializer.is_valid():
            serializer.save()
        return Response(ProductDetailSerializer(Product.objects.get(id=pk)).data)
