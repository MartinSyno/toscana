# Generated by Django 3.2.2 on 2021-05-12 15:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0006_auto_20210512_1614'),
    ]

    operations = [
        migrations.CreateModel(
            name='Images',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, upload_to='img/furniture/%Y/%m/%d')),
                ('furniture', models.ForeignKey(default=None, on_delete=django.db.models.deletion.DO_NOTHING, related_name='images', to='shop.furniture')),
            ],
        ),
    ]
