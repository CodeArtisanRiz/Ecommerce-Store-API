from django.db import models
from products.models import Products
from django.utils import timezone

# Create your models here.
# orders/models.py

# class Orders(models.Model):
#     products = models.ManyToManyField(Products)
#     order_date = models.DateTimeField(auto_now_add=True)

#     def __str__(self):
#         return f'Order {self.id} on {self.order_date}'

class Orders(models.Model):
    ORDER_STATUS_CHOICES = (
        ('P', 'Pending'),
        ('S', 'Shipped'),
        ('D', 'Delivered'),
        ('C', 'Cancelled'),
    )

    # Customer information
    customer_name = models.CharField(max_length=100, null=True, blank=True)
    customer_email = models.EmailField(null=True, blank=True)
    customer_phone = models.CharField(max_length=15, null=True, blank=True)

    # Shipping address
    shipping_address = models.TextField(null=True, blank=True)
    shipping_city = models.CharField(max_length=100, null=True, blank=True)
    shipping_state = models.CharField(max_length=100, null=True, blank=True)
    shipping_zip = models.CharField(max_length=10, null=True, blank=True)
    shipping_country = models.CharField(max_length=100, null=True, blank=True)

    # Order details
    products = models.ManyToManyField(Products)
    order_date = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=1, choices=ORDER_STATUS_CHOICES, default='P')
    total_price = models.DecimalField(max_digits=10, decimal_places=2, null=True)

    # Payment information
    payment_method = models.CharField(max_length=50, null=True, blank=True)
    payment_status = models.CharField(max_length=50, default='Pending')

    def __str__(self):
        return f'Order {self.id} by {self.customer_name}'
