# Generated by Django 3.2.5 on 2021-08-01 08:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0002_product_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='shoppingitem',
            name='product_pk',
            field=models.IntegerField(default='1'),
            preserve_default=False,
        ),
    ]
