# Generated by Django 3.2.2 on 2021-05-16 15:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0009_furniture_size'),
    ]

    operations = [
        migrations.AddField(
            model_name='furniture',
            name='old_price',
            field=models.DecimalField(decimal_places=2, default=150, max_digits=10),
            preserve_default=False,
        ),
    ]
