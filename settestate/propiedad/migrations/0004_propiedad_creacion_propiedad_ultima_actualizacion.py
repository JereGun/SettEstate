# Generated by Django 5.1.5 on 2025-02-03 01:19

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('propiedad', '0003_rename_tipo_atributo_tipo_dato'),
    ]

    operations = [
        migrations.AddField(
            model_name='propiedad',
            name='creacion',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='propiedad',
            name='ultima_actualizacion',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
