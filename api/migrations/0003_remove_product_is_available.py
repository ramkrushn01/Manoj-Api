# Generated by Django 5.0.1 on 2024-05-26 10:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_product_is_available'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='is_available',
        ),
    ]
