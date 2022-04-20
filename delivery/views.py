from rest_framework.response import Response
from rest_framework.views import APIView

from .models import DeliveryService, DeliveryMan
from .serializers import DeliveryServiceSerializer, DeliveryServiceListSerializer, DeliveryServiceDetailSerializer, \
    DeliveryManSerializer, DeliveryManListSerializer, DeliveryManDetailSerializer


class DeliveryServiceView(APIView):

    def get(self, request):
        delivery_service = DeliveryService.objects
        serializer = DeliveryServiceListSerializer(delivery_service, many=True)
        return Response(serializer.data)

    def post(self, request):
        delivery_service = DeliveryServiceSerializer(data=request.data)
        if delivery_service.is_valid():
            delivery_service.save()
            return Response(status=201)
        else:
            return Response(status=400)


class DeliveryServiceDetailView(APIView):

    def get(self, request, pk):
        delivery_service = DeliveryService.objects.get(id=pk)
        serializer = DeliveryServiceDetailSerializer(delivery_service)
        return Response(serializer.data)

    def delete(self, request, pk):
        delivery_service = DeliveryService.objects.get(id=pk)
        delivery_service.delete()
        return Response(status=201)

    def put(self, request, pk):
        delivery_service = DeliveryService.objects.get(id=pk)
        serializer = DeliveryServiceDetailSerializer(delivery_service, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(DeliveryServiceDetailSerializer(DeliveryService.objects.get(id=pk)).data)
        else:
            return Response(status=400)


class DeliveryManView(APIView):

    def get(self, request):
        delivery_man = DeliveryMan.objects
        serializer = DeliveryManListSerializer(delivery_man, many=True)
        return Response(serializer.data)

    def post(self, request):
        delivery_man = DeliveryManSerializer(data=request.data)
        if delivery_man.is_valid():
            delivery_man.save()
            return Response(status=201)
        else:
            return Response(status=400)


class DeliveryManDetailView(APIView):

    def get(self, request, pk):
        delivery_man = DeliveryMan.objects.get(id=pk)
        serializer = DeliveryManDetailSerializer(delivery_man)
        return Response(serializer.data)

    def delete(self, request, pk):
        delivery_man = DeliveryMan.objects.get(id=pk)
        delivery_man.delete()
        return Response(status=201)

    def put(self, request, pk):
        delivery_man = DeliveryMan.objects.get(id=pk)
        serializer = DeliveryManSerializer(delivery_man, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(DeliveryManDetailSerializer(DeliveryMan.objects.get(id=pk)).data)
        else:
            return Response(status=400)
