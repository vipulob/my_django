# Generated by Django 4.2.5 on 2023-12-02 16:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('carcompare', '0003_rename_car_type_car_car_typ'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='car',
            name='car_typ',
        ),
    ]