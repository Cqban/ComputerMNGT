# Generated by Django 4.2.1 on 2023-06-05 14:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('computerApp', '0021_alter_machine_maintenancedate'),
    ]

    operations = [
        migrations.AddField(
            model_name='machine',
            name='responsable',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='computerApp.personnel'),
        ),
        migrations.AlterField(
            model_name='machine',
            name='maintenanceDate',
            field=models.DateField(default='2023-06-05'),
        ),
    ]
