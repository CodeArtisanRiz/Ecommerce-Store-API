from django.db import models
from django.utils import timezone

# Create your models here.
class Products(models.Model):
    STATUS_CHOICES = (
        ('A', 'Active'),
        ('D', 'Deactivated'),
    )
    id = models.AutoField(primary_key=True)
    status = models.CharField(max_length=2, choices=STATUS_CHOICES)
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.IntegerField()
    # image = models.ImageField(upload_to='products_images/')
    image = models.CharField(max_length=255)
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.name
