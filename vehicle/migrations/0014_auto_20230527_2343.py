# Generated by Django 3.2.19 on 2023-05-27 18:13

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vehicle', '0013_auto_20230527_2143'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='outtime',
            field=models.DateTimeField(default=0, null=True),
        ),
        migrations.AlterField(
            model_name='vehicle',
            name='intime',
            field=models.TimeField(default=datetime.time(18, 13, 14, 414307), null=True),
        ),
    ]
