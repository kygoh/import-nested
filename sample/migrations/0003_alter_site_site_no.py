# Generated by Django 4.0.5 on 2022-09-17 23:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sample', '0002_remove_site_address_remove_site_latitude_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='site',
            name='site_no',
            field=models.CharField(max_length=255, verbose_name='Site Number'),
        ),
    ]
