# Generated by Django 2.2 on 2019-04-28 21:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0005_remove_item_order'),
        ('orders', '0003_remove_order_items'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='items',
            field=models.ManyToManyField(related_name='order_items', to='products.Item'),
        ),
    ]
