# Generated by Django 5.1.5 on 2025-03-02 19:23

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Empresa',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('direccion', models.CharField(max_length=200)),
                ('ciudad', models.CharField(max_length=100)),
                ('provincia', models.CharField(max_length=100)),
                ('codigo_postal', models.CharField(max_length=20)),
                ('pais', models.CharField(default='Argentina', max_length=100)),
                ('cuit', models.CharField(max_length=20)),
                ('telefono', models.CharField(max_length=20)),
                ('email', models.EmailField(max_length=254)),
                ('sitio_web', models.URLField(blank=True, null=True)),
                ('metodos_pago', models.CharField(help_text='Métodos de pago aceptados, separados por comas', max_length=255)),
                ('cuenta_bancaria', models.CharField(blank=True, max_length=100, null=True)),
                ('cbu', models.CharField(blank=True, max_length=100, null=True)),
                ('alias', models.CharField(blank=True, max_length=100, null=True)),
                ('logo', models.ImageField(blank=True, null=True, upload_to='empresa/logos/')),
                ('creacion', models.DateTimeField(auto_now_add=True)),
                ('ultima_actualizacion', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'Empresa',
                'verbose_name_plural': 'Empresa',
            },
        ),
    ]
