# Generated by Django 5.0.6 on 2024-07-04 17:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_products_delete_teatypes'),
    ]

    operations = [
        migrations.AlterField(
            model_name='products',
            name='image',
            field=models.CharField(max_length=255),
        ),
    ]
