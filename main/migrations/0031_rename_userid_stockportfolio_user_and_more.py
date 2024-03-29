# Generated by Django 4.0.6 on 2022-08-16 21:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0030_delete_stockhistory'),
    ]

    operations = [
        migrations.RenameField(
            model_name='stockportfolio',
            old_name='userid',
            new_name='user',
        ),
        migrations.AlterUniqueTogether(
            name='stockportfolio',
            unique_together={('user', 'name')},
        ),
    ]
