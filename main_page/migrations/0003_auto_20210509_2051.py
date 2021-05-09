# Generated by Django 3.2.2 on 2021-05-09 17:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_page', '0002_sitesettings'),
    ]

    operations = [
        migrations.AddField(
            model_name='sitesettings',
            name='address',
            field=models.CharField(default='Ужгород, вул. Швабська, 9', max_length=30),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='sitesettings',
            name='email',
            field=models.EmailField(default='toscana@gmail.com', max_length=254),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='sitesettings',
            name='phone',
            field=models.CharField(default='+380505816328', max_length=13),
            preserve_default=False,
        ),
    ]
