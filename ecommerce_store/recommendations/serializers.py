from rest_framework import serializers
from .models import Recommendation
from products.models import Products

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Products
        fields = ['id', 'name', 'category', 'price', 'image']

class RecommendationSerializer(serializers.ModelSerializer):
    product = ProductSerializer(read_only=True)
    recommended_products = ProductSerializer(many=True, read_only=True)

    class Meta:
        model = Recommendation
        fields = ['product', 'recommended_products']
