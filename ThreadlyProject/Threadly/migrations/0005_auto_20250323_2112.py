# Generated by Django 2.2.28 on 2025-03-23 13:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Threadly', '0004_auto_20250323_2055'),
    ]

    operations = [
        migrations.AlterField(
            model_name='thread',
            name='slug',
            field=models.SlugField(blank=True, unique=True),
        ),
    ]
