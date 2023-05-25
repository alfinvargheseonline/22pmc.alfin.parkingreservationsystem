# Generated by Django 3.2.18 on 2023-05-03 12:45

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vehicle', '0003_vehicle_user_alter_vehicle_intime_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Parkings',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('parking_id', models.IntegerField()),
                ('location', models.CharField(max_length=100)),
                ('Street', models.CharField(max_length=100)),
                ('park_name', models.CharField(max_length=100)),
                ('slot', models.IntegerField()),
                ('remaning_slot', models.IntegerField()),
                ('attendant', models.CharField(max_length=100)),
                ('price', models.IntegerField()),
            ],
        ),
        migrations.AlterField(
            model_name='vehicle',
            name='intime',
            field=models.TimeField(default=datetime.time(12, 45, 57, 18409), null=True),
        ),
        migrations.AlterField(
            model_name='vehicle',
            name='pdate',
            field=models.DateField(default=datetime.date(2023, 5, 3), null=True),
        ),
    ]
