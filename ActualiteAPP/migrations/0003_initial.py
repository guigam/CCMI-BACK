# Generated by Django 4.1.12 on 2023-10-12 13:22

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('ActualiteAPP', '0002_delete_actualite'),
    ]

    operations = [
        migrations.CreateModel(
            name='Actualite',
            fields=[
                ('ActualiteId', models.AutoField(primary_key=True, serialize=False)),
                ('ActualiteTitle', models.CharField(max_length=250)),
                ('ActualiteDescription', models.CharField(max_length=500)),
            ],
        ),
    ]
