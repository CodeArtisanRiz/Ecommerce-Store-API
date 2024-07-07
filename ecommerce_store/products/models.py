from django.db import models
from django.utils import timezone

# Create your models here.
class Products(models.Model):
    STATUS_CHOICES = (
        ('A', 'Active'),
        ('D', 'Deactivated'),
    )
    CATEGORY_CHOICES = (
        ('EL', 'Electronics'),
        ('HM', 'Home & Kitchen'),
        ('BT', 'Beauty & Personal Care'),
        ('SP', 'Sports & Outdoors'),
        ('OF', 'Office Supplies'),
        ('HG', 'Health & Wellness'),
        ('BK', 'Books & Media'),
        ('TS', 'Toys & Games'),
        ('JW', 'Jewelry & Accessories'),
        ('FD', 'Food & Beverages'),
        ('NO', 'None')
    )
    id = models.AutoField(primary_key=True)
    status = models.CharField(max_length=1, choices=STATUS_CHOICES, default='D')
    name = models.CharField(max_length=100)
    description = models.TextField()
    category = models.CharField(max_length=2, choices=CATEGORY_CHOICES, default='NO')
    price = models.IntegerField()
    # image = models.ImageField(upload_to='products_images/')
    image = models.CharField(max_length=255)
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.name
