# Generated by Django 2.2.7 on 2019-11-28 04:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('company', '0002_auto_20191128_0435'),
    ]

    operations = [
        migrations.RenameField(
            model_name='company',
            old_name='GPS_y',
            new_name='GPS_Y',
        ),
    ]
