# from django.shortcuts import render
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Orders
from .serializers import OrderSerializer


# Create your views here.
class CreateOrderAPIView(generics.CreateAPIView):
    queryset = Orders.objects.all()
    serializer_class = OrderSerializer

class ViewOrderAPIView(APIView):
    def get(self, request, order_id):
        try:
            order = Orders.objects.get(id=order_id)
            serializer = OrderSerializer(order)
            return Response(serializer.data)
        except Orders.DoesNotExist:
            return Response({"error": "Order not found"}, status=404)


class OrderListView(generics.ListAPIView):
    queryset = Orders.objects.all()
    serializer_class = OrderSerializer
