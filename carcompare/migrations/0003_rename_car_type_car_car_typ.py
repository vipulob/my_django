# Generated by Django 4.2.5 on 2023-12-02 16:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('carcompare', '0002_rename_engine_liter_car_engine_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='car',
            old_name='car_type',
            new_name='car_typ',
        ),
    ]