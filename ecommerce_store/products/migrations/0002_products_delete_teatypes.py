# Generated by Django 5.0.6 on 2024-07-04 07:30

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Products',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('status', models.CharField(choices=[('A', 'Active'), ('D', 'Deactivated')], max_length=2)),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('price', models.IntegerField()),
                ('image', models.ImageField(upload_to='products_images/')),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('updated_at', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
        migrations.DeleteModel(
            name='TeaTypes',
        ),
    ]
