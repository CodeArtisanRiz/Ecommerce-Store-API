# Generated by Django 5.0.6 on 2024-07-06 10:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0005_alter_products_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='products',
            name='category',
            field=models.CharField(choices=[('EL', 'Electronics'), ('HM', 'Home & Kitchen'), ('BT', 'Beauty & Personal Care'), ('SP', 'Sports & Outdoors'), ('OF', 'Office Supplies'), ('HG', 'Health & Wellness'), ('BK', 'Books & Media'), ('TS', 'Toys & Games'), ('JW', 'Jewelry & Accessories'), ('FD', 'Food & Beverages'), ('NO', 'None')], default='NO', max_length=2),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='products',
            name='status',
            field=models.CharField(choices=[('A', 'Active'), ('D', 'Deactivated')], default='NO', max_length=2),
        ),
    ]
