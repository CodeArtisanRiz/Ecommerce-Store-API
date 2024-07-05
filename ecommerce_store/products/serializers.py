from rest_framework import serializers
from .models import Products

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Products
        fields = ['id', 'status', 'name', 'description', 'price', 'image', 'created_at', 'updated_at']
