# Generated by Django 4.1.12 on 2023-10-14 19:24

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ActualiteAPP', '0007_actualite_actualitestatus_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Service',
            fields=[
                ('ServiceId', models.AutoField(primary_key=True, serialize=False)),
                ('ServiceTitle', models.CharField(max_length=250)),
                ('ServiceDescription', models.CharField(max_length=500)),
            ],
        ),
        migrations.AlterField(
            model_name='actualite',
            name='ActualiteDate',
            field=models.DateTimeField(default=datetime.datetime(2023, 10, 14, 19, 24, 57, 191354, tzinfo=datetime.timezone.utc)),
        ),
    ]