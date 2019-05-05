# Generated by Django 2.2 on 2019-04-28 20:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0003_remove_order_items'),
        ('products', '0002_remove_product_order'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='order',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='orders.Order'),
        ),
        migrations.AlterField(
            model_name='item',
            name='type_unity',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='products.TypeUnity'),
        ),
    ]
