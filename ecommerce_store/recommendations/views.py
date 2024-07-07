from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Recommendation
from products.models import Products
from .serializers import RecommendationSerializer, ProductSerializer
from django.shortcuts import get_object_or_404
import random

class RecommendationView(APIView):
    # GET method for product recommendations
    def get(self, request, product_id):
        # Get the product object for the given product_id
        product = get_object_or_404(Products, id=product_id)
        try:
            # Try to get the Recommendation object for the product
            recommendation = Recommendation.objects.get(product=product)
            # Get the list of recommended products
            recommended_products = list(recommendation.recommended_products.all())

            # If there are less than 5 recommended products
            if len(recommended_products) < 5:
                # Calculate the remaining number of products needed
                remaining_products = 5 - len(recommended_products)
                # Get a list of random products from the same category, excluding the current product
                random_products = list(Products.objects.filter(category=product.category).exclude(id=product_id).order_by('?'))
                # Add the random products to the recommended products list
                recommended_products.extend(random.sample(random_products, remaining_products))

            # Serialize the recommendation and recommended products
            response_data = RecommendationSerializer(recommendation).data
            response_data['recommended_products'] = ProductSerializer(recommended_products, many=True).data
        except Recommendation.DoesNotExist:
            # If no recommendation exists
            # Get 5 random products from the same category, excluding current
            category_products = Products.objects.filter(category=product.category).exclude(id=product_id).order_by('?')[:5]
            # Create the response data with the product details
            response_data = {
                "product": {
                    "id": product.id,
                    "name": product.name,
                    "category": product.category,
                    "price": product.price,
                    "image": product.image.url
                },
                "recommended_products": ProductSerializer(category_products, many=True).data
            }

        # Return the response
        return Response(response_data, status=status.HTTP_200_OK)
