# Generated by Django 4.0.5 on 2022-07-25 20:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0014_stockportfolio_description_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='stockportfolio',
            old_name='username',
            new_name='userid',
        ),
        migrations.AlterUniqueTogether(
            name='stockportfolio',
            unique_together={('userid', 'portfolio_name')},
        ),
    ]
