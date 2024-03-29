# Generated by Django 4.0.5 on 2022-07-13 13:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_remove_stock_id_alter_stock_ticker'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stock',
            name='business_summary',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='stock',
            name='city',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='stock',
            name='country',
            field=models.CharField(max_length=60, null=True),
        ),
        migrations.AlterField(
            model_name='stock',
            name='currency_unit',
            field=models.CharField(max_length=5, null=True),
        ),
        migrations.AlterField(
            model_name='stock',
            name='current_price',
            field=models.DecimalField(decimal_places=8, max_digits=19, null=True),
        ),
        migrations.AlterField(
            model_name='stock',
            name='day_low',
            field=models.DecimalField(decimal_places=8, max_digits=19, null=True),
        ),
        migrations.AlterField(
            model_name='stock',
            name='fifty_day_average',
            field=models.DecimalField(decimal_places=8, max_digits=19, null=True),
        ),
        migrations.AlterField(
            model_name='stock',
            name='industry',
            field=models.CharField(max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='stock',
            name='logo_url',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='stock',
            name='long_name',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='stock',
            name='pre_market_price',
            field=models.DecimalField(decimal_places=8, max_digits=19, null=True),
        ),
        migrations.AlterField(
            model_name='stock',
            name='regular_market_day_high',
            field=models.DecimalField(decimal_places=8, max_digits=19, null=True),
        ),
        migrations.AlterField(
            model_name='stock',
            name='regular_market_open',
            field=models.DecimalField(decimal_places=8, max_digits=19, null=True),
        ),
        migrations.AlterField(
            model_name='stock',
            name='regular_market_previous_close',
            field=models.DecimalField(decimal_places=8, max_digits=19, null=True),
        ),
        migrations.AlterField(
            model_name='stock',
            name='regular_market_price',
            field=models.DecimalField(decimal_places=8, max_digits=19, null=True),
        ),
        migrations.AlterField(
            model_name='stock',
            name='state',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='stock',
            name='two_hundred_day_average',
            field=models.DecimalField(decimal_places=8, max_digits=19, null=True),
        ),
        migrations.AlterField(
            model_name='stock',
            name='website',
            field=models.TextField(null=True),
        ),
    ]
