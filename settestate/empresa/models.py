from django.db import models
from django.core.exceptions import ValidationError

class Empresa(models.Model):
    """
    Modelo para almacenar la información de la empresa.
    Se implementa como un singleton para asegurar que solo haya una instancia.
    """
    nombre = models.CharField(max_length=100)
    direccion = models.CharField(max_length=200)
    ciudad = models.CharField(max_length=100)
    provincia = models.CharField(max_length=100)
    codigo_postal = models.CharField(max_length=20)
    pais = models.CharField(max_length=100, default='Argentina')
    cuit = models.CharField(max_length=20)
    telefono = models.CharField(max_length=20)
    email = models.EmailField()
    sitio_web = models.URLField(blank=True, null=True)
    
    # Información bancaria
    metodos_pago = models.CharField(max_length=255, help_text="Métodos de pago aceptados, separados por comas", blank=True, null=True)
    cuenta_bancaria = models.CharField(max_length=100, blank=True, null=True)
    cbu = models.CharField(max_length=100, blank=True, null=True)
    alias = models.CharField(max_length=100, blank=True, null=True)
    
    # Logo de la empresa
    logo = models.ImageField(upload_to='media/empresa/logo/', blank=True, null=True)
    
    # Campos de auditoría
    creacion = models.DateTimeField(auto_now_add=True)
    ultima_actualizacion = models.DateTimeField(auto_now=True)
    
    class Meta:
        verbose_name = 'Empresa'
        verbose_name_plural = 'Empresa'
    
    def save(self, *args, **kwargs):
        """
        Asegura que solo exista una instancia de Empresa (patrón Singleton)
        """
        if not self.pk and Empresa.objects.exists():
            raise ValidationError('Ya existe una empresa registrada. Solo puede haber una.')
        return super().save(*args, **kwargs)
    
    def __str__(self):
        return self.nombre

