# Generated by Django 2.2.5 on 2020-11-09 04:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('postapp', '0002_auto_20201108_1704'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='hashtags',
            field=models.TextField(blank=True),
        ),
    ]
