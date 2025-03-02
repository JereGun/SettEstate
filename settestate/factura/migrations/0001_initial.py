# Generated by Django 5.1.5 on 2025-02-14 02:07

import django.core.validators
import django.db.models.deletion
from decimal import Decimal
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('contrato', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Factura',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('numero', models.CharField(max_length=20, unique=True)),
                ('fecha_emision', models.DateField()),
                ('fecha_vencimiento', models.DateField()),
                ('estado', models.CharField(choices=[('BORRADOR', 'Borrador'), ('EMITIDA', 'Emitida'), ('ANULADA', 'Anulada'), ('PAGADA', 'Pagada')], default='BORRADOR', max_length=10)),
                ('total', models.DecimalField(decimal_places=2, max_digits=10, validators=[django.core.validators.MinValueValidator(Decimal('0.00'))])),
                ('creacion', models.DateTimeField(auto_now_add=True)),
                ('modificacion', models.DateTimeField(auto_now=True)),
                ('contrato', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='contrato.contrato')),
            ],
            options={
                'verbose_name': 'Factura',
                'verbose_name_plural': 'Facturas',
            },
        ),
        migrations.CreateModel(
            name='ItemFactura',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipo', models.CharField(choices=[('ALQUILER', 'Alquiler'), ('EXPENSAS', 'Expensas'), ('SERVICIO', 'Servicio'), ('IMPUESTO', 'Impuesto'), ('OTRO', 'Otro')], max_length=10)),
                ('descripcion', models.CharField(max_length=100)),
                ('monto', models.DecimalField(decimal_places=2, max_digits=10, validators=[django.core.validators.MinValueValidator(Decimal('0.00'))])),
                ('subtotal', models.DecimalField(decimal_places=2, max_digits=10, validators=[django.core.validators.MinValueValidator(Decimal('0.00'))])),
                ('factura', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='items', to='factura.factura')),
            ],
            options={
                'verbose_name': 'ItemFactura',
                'verbose_name_plural': 'ItemFacturas',
            },
        ),
    ]
