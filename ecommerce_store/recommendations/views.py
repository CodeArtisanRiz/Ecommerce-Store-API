from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Recommendation
from products.models import Products
from .serializers import RecommendationSerializer, ProductSerializer
from django.shortcuts import get_object_or_404
import random

class RecommendationView(APIView):
    def get(self, request, product_id):
        product = get_object_or_404(Products, id=product_id)
        try:
            recommendation = Recommendation.objects.get(product=product)
            response_data = RecommendationSerializer(recommendation).data
        except Recommendation.DoesNotExist:
            category_products = Products.objects.filter(category=product.category).exclude(id=product_id).order_by('?')[:5]
            response_data = {
                "product": {
                    "id": product.id,
                    "name": product.name,
                    "category": product.category,
                    "price": product.price,
                    "image": product.image.url if product.image else None
                },
                "recommended_products": ProductSerializer(category_products, many=True).data
            }

        return Response(response_data, status=status.HTTP_200_OK)
