# Generated by Django 3.2.2 on 2021-05-16 19:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='code',
            field=models.IntegerField(auto_created=True, default=12345, verbose_name=8495322622436),
            preserve_default=False,
        ),
    ]
