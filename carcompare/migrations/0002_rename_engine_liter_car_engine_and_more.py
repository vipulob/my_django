# Generated by Django 4.2.5 on 2023-12-02 16:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('carcompare', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='car',
            old_name='engine_liter',
            new_name='engine',
        ),
        migrations.RenameField(
            model_name='car',
            old_name='ncap_rating',
            new_name='gncap_rating',
        ),
        migrations.AlterField(
            model_name='car',
            name='car_type',
            field=models.CharField(max_length=25, null=True),
        ),
        migrations.AlterField(
            model_name='car',
            name='manufacturer',
            field=models.CharField(max_length=25, null=True),
        ),
    ]
