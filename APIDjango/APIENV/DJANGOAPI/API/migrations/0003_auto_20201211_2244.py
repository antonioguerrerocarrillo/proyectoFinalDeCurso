# Generated by Django 3.1.4 on 2020-12-11 21:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('API', '0002_auto_20201211_2234'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cita',
            name='fecha',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
