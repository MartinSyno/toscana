# Generated by Django 3.2.3 on 2021-05-24 05:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0017_remove_category_photo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='photos',
            name='furniture',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='photos', to='shop.furniture'),
        ),
    ]
