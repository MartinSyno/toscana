# Generated by Django 3.2.2 on 2021-05-08 20:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0004_category_photo'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'ordering': ('name',)},
        ),
        migrations.AddField(
            model_name='category',
            name='slug',
            field=models.SlugField(default='no_slug'),
            preserve_default=False,
        ),
        migrations.AlterIndexTogether(
            name='category',
            index_together={('id', 'slug')},
        ),
    ]
