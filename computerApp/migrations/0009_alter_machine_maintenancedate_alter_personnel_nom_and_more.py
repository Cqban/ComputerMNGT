# Generated by Django 4.1.7 on 2023-05-08 11:18

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('computerApp', '0008_alter_machine_maintenancedate'),
    ]

    operations = [
        migrations.AlterField(
            model_name='machine',
            name='maintenanceDate',
            field=models.DateField(default=datetime.datetime(2023, 5, 8, 11, 18, 10, 497571)),
        ),
        migrations.AlterField(
            model_name='personnel',
            name='nom',
            field=models.CharField(max_length=8),
        ),
        migrations.AlterField(
            model_name='personnel',
            name='prenom',
            field=models.CharField(max_length=8),
        ),
    ]