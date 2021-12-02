# Generated by Django 3.2.5 on 2021-08-05 18:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0004_remove_shoppingitem_product_pk'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shoppingitem',
            name='shopping_cart',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='items', to='shop.shoppingcart'),
        ),
    ]
