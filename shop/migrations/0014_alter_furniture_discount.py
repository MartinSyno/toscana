# Generated by Django 3.2.2 on 2021-05-16 15:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0013_alter_furniture_discount'),
    ]

    operations = [
        migrations.AlterField(
            model_name='furniture',
            name='discount',
            field=models.IntegerField(blank=True),
        ),
    ]