# Generated by Django 4.0.6 on 2022-08-17 22:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0033_trade_purchase_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='trade',
            name='quantity',
            field=models.DecimalField(decimal_places=3, max_digits=10),
        ),
    ]