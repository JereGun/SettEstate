from django.db import models
from persona.models import Persona

class Propiedad(models.Model):
    TIPOS = [
        ('CASA', 'Casa'),
        ('DEPARTAMENTO', 'Departamento'),
        ('LOCAL COMERCIAL', 'Local Comercial'),
        ('OFICINA', 'Oficina'),
        ('TERRENO', 'Terreno'),
        ('GALPON', 'Galpón'),
        ('FONDO DE COMERCIO', 'Fondo de Comercio'),
        ('HOTEL', 'Hotel'),
        ('COCHERA', 'Cochera'),
        ('OTRO', 'Otro'),
    ]
    
    TIPO_TRANSACCION = [
        ('ALQUILER', 'Alquiler'),
        ('VENTA', 'Venta'),
        ('ALQUILER/VENTA', 'Alquiler/Venta'),
    ]

    """Model definition for Propiedad."""
    nombre = models.CharField(max_length=50)
    calle = models.CharField(max_length=100)
    dueño = models.ForeignKey(Persona, on_delete=models.CASCADE, blank=True, null=True)
    numeracion = models.CharField(max_length=10, blank=True, null=True, default='S/N')
    piso = models.CharField(max_length=5, blank=True, null=True)
    departamento = models.CharField(max_length=5, blank=True, null=True)
    ciudad = models.CharField(max_length=50, default='Córdoba')
    provincia = models.CharField(max_length=50, default='Córdoba')
    pais = models.CharField(max_length=50, default='Argentina')
    descripcion = models.TextField(null=True, blank=True)
    tipo = models.CharField(max_length=20, choices=TIPOS)
    disponible = models.BooleanField(default=True)
    alquiler_venta = models.CharField(max_length=15, choices=TIPO_TRANSACCION)
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    baños = models.IntegerField(default=1)
    dormitorios = models.IntegerField(default=1)
    habitaciones = models.IntegerField(default=1)
    cocheras = models.IntegerField(default=0, null=True, blank=True)
    metros_cuadrados = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    pisos = models.IntegerField(default=1, null=True, blank=True)
    antiguedad = models.IntegerField(default=0, null=True, blank=True)
    piscina = models.BooleanField(default=False)
    creacion = models.DateTimeField(auto_now_add=True)
    ultima_actualizacion = models.DateTimeField(auto_now=True)


    # TODO: Define fields here

    class Meta:
        """Meta definition for Propiedad."""
        verbose_name = 'Propiedad'
        verbose_name_plural = 'Propiedades'

    def __str__(self):
        """Unicode representation of Propiedad."""
        return f'{self.nombre} - {self.tipo} - {self.alquiler_venta} - ${self.precio}'


