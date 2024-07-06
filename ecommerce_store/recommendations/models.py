from django.db import models
from products.models import Products

class Recommendation(models.Model):
    product = models.OneToOneField(Products, on_delete=models.CASCADE, related_name='product_recommendations')
    recommended_products = models.ManyToManyField(Products, related_name='recommended_for_product')
    score = models.FloatField(default=0.0)  # Optional: to store a recommendation score

    def __str__(self):
        return f"Recommendations for {self.product.name}"
