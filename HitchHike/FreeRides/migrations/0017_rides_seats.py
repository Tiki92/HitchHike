# Generated by Django 2.2 on 2019-06-22 08:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('FreeRides', '0016_localusers_department'),
    ]

    operations = [
        migrations.AddField(
            model_name='rides',
            name='seats',
            field=models.PositiveIntegerField(default=1, null=True),
        ),
    ]