# Generated by Django 3.0.8 on 2020-08-18 20:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_auto_20200817_1409'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='header_image_subtitle',
            field=models.CharField(blank=True, max_length=500),
        ),
    ]
