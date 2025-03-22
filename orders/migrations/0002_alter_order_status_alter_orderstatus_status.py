# Generated by Django 5.1.7 on 2025-03-20 22:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='status',
            field=models.CharField(choices=[('Preparing', 'Preparing'), ('Out for Delivery', 'Out for Delivery'), ('Delivered', 'Delivered'), ('cancelled', 'Cancelled')], default='pending', max_length=20),
        ),
        migrations.AlterField(
            model_name='orderstatus',
            name='status',
            field=models.CharField(choices=[('Preparing', 'Preparing'), ('Out for Delivery', 'Out for Delivery'), ('Delivered', 'Delivered'), ('cancelled', 'Cancelled')], default='Preparing', max_length=20),
        ),
    ]
