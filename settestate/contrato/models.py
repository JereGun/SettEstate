from django.db import models
from django.utils import timezone
from persona.models import Persona
from propiedad.models import Propiedad

class Contrato(models.Model):
    FRECUENCIA_ACTUALIZACION = [
        ('MENSUAL', 'Mensual'),
        ('BIMESTRAL', 'Bimestral'),
        ('TRIMESTRAL', 'Trimestral'),
        ('SEMESTRAL', 'Semestral'),
        ('ANUAL', 'Anual')
    ]
    """Model definition for Contrato."""
    inquilino = models.ForeignKey(Persona, on_delete=models.CASCADE)
    propiedad = models.ForeignKey(Propiedad, on_delete=models.CASCADE)
    fecha_inicio = models.DateField()
    fecha_fin = models.DateField()
    frecuencia_actualizacion = models.CharField(max_length=10, choices=FRECUENCIA_ACTUALIZACION)
    ultima_actualizacion = models.DateTimeField(auto_now=True, null=True, blank=True)

    # TODO: Define fields here

    class Meta:
        """Meta definition for Contrato."""

        verbose_name = 'Contrato'
        verbose_name_plural = 'Contratos'

    def __str__(self):
        """Unicode representation of Contrato."""
        return f'Contrato de {self.propiedad.nombre} - {self.inquilino.nombre_completo()} - {self.fecha_inicio} hasta {self.fecha_fin}'

class ActualizacionAlquiler(models.Model):
    """Model definition for ActualziacionAlquiler."""
    contrato = models.ForeignKey(Contrato, on_delete=models.CASCADE)
    fecha_actualizacion = models.DateField(default=timezone.now)
    porcentaje_aumento = models.DecimalField(max_digits=5, decimal_places=2) # Porcentaje del aumento
    nuevo_precio = models.DecimalField(max_digits=10, decimal_places=2) # Precio actualizado despues del aumento

    # TODO: Define fields here

    class Meta:
        """Meta definition for ActualziacionAlquiler."""

        verbose_name = 'Actualziacion de Alquiler'
        verbose_name_plural = 'Actualziaciones de Alquileres'

    def __str__(self):
        """Unicode representation of ActualziacionAlquiler."""
        return f"Actualización del {self.fecha_actualizacion} ({self.porcentaje_aumento}%)"
    
    def save(self, *args, **kwargs):
        # Calcular el nuevo precio basado en el porcentaje de aumento
        self.nuevo_precio = self.contrato.propiedad.precio * (1 + self.porcentaje_aumento / 100)
        super().save(*args, **kwargs)

        # Actualizar el precio de alquiler en la propiedad
        self.contrato.propiedad.precio_alquiler = self.nuevo_precio
        self.contrato.propiedad.save()

        # Actualizar la fecha de última actualización en el contrato
        self.contrato.ultima_actualizacion = self.fecha_actualizacion
        self.contrato.save()