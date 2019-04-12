# Generated by Django 2.1.7 on 2019-03-05 21:13

import django.contrib.gis.db.models.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Rides',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('location_name', models.CharField(max_length=20)),
                ('location', django.contrib.gis.db.models.fields.PointField(srid=1234)),
                ('destination_name', models.CharField(max_length=20)),
                ('destination', django.contrib.gis.db.models.fields.PointField(srid=1235)),
            ],
            options={
                'verbose_name_plural': ' Rides',
            },
        ),
    ]
