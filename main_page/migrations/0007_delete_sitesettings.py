# Generated by Django 3.2.3 on 2021-05-17 11:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main_page', '0006_sitesettings_working_hours'),
    ]

    operations = [
        migrations.DeleteModel(
            name='SiteSettings',
        ),
    ]
