# Generated by Django 3.2.19 on 2023-05-30 18:13

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vehicle', '0015_auto_20230527_2355'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vehicle',
            name='intime',
            field=models.TimeField(default=datetime.time(18, 13, 21, 583908), null=True),
        ),
        migrations.AlterField(
            model_name='vehicle',
            name='pdate',
            field=models.DateField(default=datetime.date(2023, 5, 30), null=True),
        ),
    ]