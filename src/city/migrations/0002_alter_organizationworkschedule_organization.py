# Generated by Django 5.0.2 on 2024-03-13 07:52

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('city', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='organizationworkschedule',
            name='organization',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='city.organization'),
        ),
    ]
