# Generated by Django 4.0.5 on 2022-07-26 20:29

from django.db import migrations, models
import main.models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0018_rename_portfolio_name_stockportfolio_name_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='cover_image',
            field=models.ImageField(blank=True, null=True, upload_to=main.models.user_directory_path),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='profile_picture',
            field=models.ImageField(blank=True, null=True, upload_to=main.models.user_directory_path),
        ),
    ]
