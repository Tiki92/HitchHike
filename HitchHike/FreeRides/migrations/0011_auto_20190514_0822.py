# Generated by Django 2.2 on 2019-05-14 08:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('FreeRides', '0010_auto_20190512_1036'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rides',
            name='ride_date',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]