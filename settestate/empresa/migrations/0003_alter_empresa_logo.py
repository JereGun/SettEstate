# Generated by Django 5.1.5 on 2025-03-03 05:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('empresa', '0002_alter_empresa_metodos_pago'),
    ]

    operations = [
        migrations.AlterField(
            model_name='empresa',
            name='logo',
            field=models.ImageField(blank=True, null=True, upload_to='media/empresa/logo/'),
        ),
    ]
