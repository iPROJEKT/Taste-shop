# Generated by Django 2.2.16 on 2023-09-25 13:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cardshopitem',
            name='group',
        ),
        migrations.AddField(
            model_name='cardshopitem',
            name='slug',
            field=models.SlugField(default=1, max_length=255, unique=True, verbose_name='URL'),
            preserve_default=False,
        ),
        migrations.DeleteModel(
            name='Group',
        ),
    ]
