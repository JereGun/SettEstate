# Generated by Django 5.1.5 on 2025-02-02 04:55

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Persona',
            fields=[
                ('documento', models.CharField(max_length=9, primary_key=True, serialize=False, unique=True, validators=[django.core.validators.RegexValidator(message='El documento debe tener 9 caracteres', regex='^[0-9]*$')])),
                ('nombre', models.CharField(max_length=50)),
                ('apellido', models.CharField(max_length=50)),
                ('fecha_nacimiento', models.DateField()),
                ('direccion', models.CharField(max_length=100)),
                ('ciudad', models.CharField(max_length=50)),
                ('provincia', models.CharField(max_length=50)),
                ('pais', models.CharField(max_length=50)),
                ('telefono', models.CharField(max_length=20, validators=[django.core.validators.RegexValidator(message='El teléfono debe tener solo números', regex='^[0-9]*$')])),
                ('email', models.EmailField(max_length=100)),
            ],
            options={
                'verbose_name': 'Persona',
                'verbose_name_plural': 'Personas',
            },
        ),
    ]
