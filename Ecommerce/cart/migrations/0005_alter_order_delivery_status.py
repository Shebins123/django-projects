# Generated by Django 4.2.1 on 2023-06-05 06:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0004_remove_order_totalprice'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='delivery_status',
            field=models.CharField(default='pending', max_length=30),
        ),
    ]
