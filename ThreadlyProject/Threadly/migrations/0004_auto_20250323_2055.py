# Generated by Django 2.2.28 on 2025-03-23 12:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Threadly', '0003_auto_20250323_2049'),
    ]

    operations = [
        migrations.AlterField(
            model_name='thread',
            name='slug',
            field=models.SlugField(blank=True, default='default-slug', unique=True),
        ),
    ]
