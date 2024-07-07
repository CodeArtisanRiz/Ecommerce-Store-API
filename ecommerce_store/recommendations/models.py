from django.db import models
from products.models import Products


class Recommendation(models.Model):
    # Get product for recommendations.
    product = models.OneToOneField(Products, on_delete=models.CASCADE, related_name='product_recommendations')

    # List of recommended products for the given product
    recommended_products = models.ManyToManyField(Products, related_name='recommended_for_product')

    # An optional score to store the recommendation strength or relevance
    score = models.FloatField(default=0.0)

    def __str__(self):
        return f"Recommendations for {self.product.name}"
