# Generated by Django 4.1.3 on 2023-05-10 09:42

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vehicle', '0005_rename_street_parkings_street_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vehicle',
            name='intime',
            field=models.TimeField(default=datetime.time(9, 42, 55, 932070), null=True),
        ),
        migrations.AlterField(
            model_name='vehicle',
            name='pdate',
            field=models.DateField(default=datetime.date(2023, 5, 10), null=True),
        ),
    ]