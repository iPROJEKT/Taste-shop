# Generated by Django 2.2.16 on 2023-07-22 09:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0011_auto_20230721_2156'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='group',
            name='gif_m',
        ),
    ]
