# Generated by Django 3.2.3 on 2021-05-24 05:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_page', '0008_sitesettings'),
    ]

    operations = [
        migrations.AlterField(
            model_name='banner',
            name='photo',
            field=models.ImageField(upload_to='img/banner'),
        ),
    ]
