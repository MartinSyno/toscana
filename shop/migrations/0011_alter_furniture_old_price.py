# Generated by Django 3.2.2 on 2021-05-16 15:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0010_furniture_old_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='furniture',
            name='old_price',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10),
        ),
    ]
