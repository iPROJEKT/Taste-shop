# Generated by Django 2.2.16 on 2023-07-21 18:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0007_auto_20230721_1818'),
    ]

    operations = [
        migrations.AddField(
            model_name='group',
            name='gif',
            field=models.ImageField(default=None, upload_to='grup/gif/'),
        ),
        migrations.AlterField(
            model_name='cardshopitem',
            name='image',
            field=models.ImageField(upload_to='shouse/'),
        ),
        migrations.AlterField(
            model_name='group',
            name='image',
            field=models.ImageField(default=None, upload_to='grup/img'),
        ),
    ]
