# Generated by Django 5.0.2 on 2024-03-04 17:17

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Organization',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('description', models.CharField(max_length=2048)),
                ('type', models.IntegerField()),
                ('rating', models.IntegerField()),
                ('lat', models.DecimalField(decimal_places=15, max_digits=20)),
                ('lon', models.DecimalField(decimal_places=15, max_digits=20)),
            ],
        ),
        migrations.CreateModel(
            name='OrganizationWorkSchedule',
            fields=[
                ('day_of_week', models.IntegerField()),
                ('organization', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='city.organization')),
                ('start', models.IntegerField()),
                ('finish', models.IntegerField()),
            ],
            options={
                'db_table': 'city_organization_work_schedule',
            },
        ),
        migrations.CreateModel(
            name='OrganizationTag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('organization', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='city.organization')),
            ],
            options={
                'db_table': 'city_organization_tag',
            },
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('organization', models.ManyToManyField(through='city.OrganizationTag', to='city.organization')),
            ],
        ),
        migrations.AddField(
            model_name='organizationtag',
            name='tag',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='city.tag'),
        ),
    ]