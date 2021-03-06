# Generated by Django 3.2.2 on 2021-05-16 22:33

from django.db import migrations, models
import orders.models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0005_alter_order_code'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='code',
            field=models.IntegerField(default=orders.models.Order.random_number),
        ),
        migrations.AlterField(
            model_name='order',
            name='first_name',
            field=models.CharField(auto_created=True, max_length=50),
        ),
    ]
