# Generated by Django 3.2.2 on 2021-05-13 09:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0008_auto_20210512_1836'),
    ]

    operations = [
        migrations.AddField(
            model_name='furniture',
            name='size',
            field=models.CharField(default='30x30x15 см', max_length=30),
            preserve_default=False,
        ),
    ]
