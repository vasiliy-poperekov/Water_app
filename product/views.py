from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Product
from .serializers import ProductListSerializer, ProductDetailSerializer, ProductSerializer


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
