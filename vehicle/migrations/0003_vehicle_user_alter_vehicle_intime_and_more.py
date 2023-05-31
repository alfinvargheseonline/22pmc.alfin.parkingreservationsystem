# Generated by Django 4.1.3 on 2023-04-14 11:20

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('vehicle', '0002_user_details_user_login'),
    ]

    operations = [
        migrations.AddField(
            model_name='vehicle',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='vehicle.user_login'),
        ),
        migrations.AlterField(
            model_name='vehicle',
            name='intime',
            field=models.TimeField(default=datetime.time(11, 20, 52, 292931), null=True),
        ),
        migrations.AlterField(
            model_name='vehicle',
            name='outtime',
            field=models.TimeField(null=True),
        ),
        migrations.AlterField(
            model_name='vehicle',
            name='pdate',
            field=models.DateField(default=datetime.date(2023, 4, 14), null=True),
        ),
    ]
