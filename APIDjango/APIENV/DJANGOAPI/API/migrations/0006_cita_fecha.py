# Generated by Django 3.1.4 on 2020-12-11 22:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('API', '0005_remove_cita_fecha'),
    ]

    operations = [
        migrations.AddField(
            model_name='cita',
            name='fecha',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]
