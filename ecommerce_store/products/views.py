from django.http import HttpResponse
from django.shortcuts import render

from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Products
from .serializers import ProductSerializer

# Create your views here.
def products(request):
    return HttpResponse("Products. You're at products page.")

class ProductListView(APIView):
    def get(self, request):
        products = Products.objects.all()
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data, status=200, content_type='application/json')

class AddProductView(APIView):
    def post(self, request):
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "Product added successfully"}, status=201)
        return Response(serializer.errors, status=400)

class ViewProductAPIView(APIView):
    def get(self, request, pro_id):
        try:
            product = Products.objects.get(id=pro_id)
            serializer = ProductSerializer(product)
            return Response(serializer.data)
        except Products.DoesNotExist:
            return Response({"error": "Product not found"}, status=404)