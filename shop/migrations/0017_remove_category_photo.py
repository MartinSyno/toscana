# Generated by Django 3.2.3 on 2021-05-24 05:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0016_auto_20210524_0852'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='category',
            name='photo',
        ),
    ]