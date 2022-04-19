from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Consumer
from .serializers import ConsumerListSerializer, ConsumerDetailSerializer


class ConsumerView(APIView):

    def get(self, request):
        consumers = Consumer.objects
        serializer = ConsumerListSerializer(consumers, many=True)
        return Response(serializer.data)

    def post(self, request):
        consumer = ConsumerDetailSerializer(data=request.data)
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
        serializer = ConsumerDetailSerializer(consumer, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(ConsumerDetailSerializer(Consumer.objects.get(id=pk)).data)
        else:
            return Response(status=400)
