# Generated by Django 4.0.5 on 2022-07-13 13:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_stock'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='stock',
            name='id',
        ),
        migrations.AlterField(
            model_name='stock',
            name='ticker',
            field=models.CharField(max_length=5, primary_key=True, serialize=False),
        ),
    ]
