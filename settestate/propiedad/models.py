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
    #
    denominacion = models.CharField(max_length=50)
    tipo = models.CharField(max_length=20, choices=TIPOS)
    descripcion = models.TextField(null=True, blank=True)
    # Locador
    dueño = models.ForeignKey(Persona, on_delete=models.CASCADE, blank=True, null=True)
    # Ubicacion
    calle = models.CharField(max_length=100)
    numeracion = models.CharField(max_length=10, blank=True, null=True, default='S/N')
    piso = models.CharField(max_length=5, blank=True, null=True) # En el caso de ser Departamento
    departamento = models.CharField(max_length=5, blank=True, null=True) # En el caso de ser Departamento
    barrio = models.CharField(max_length=50)
    ciudad = models.CharField(max_length=50, default='Córdoba')
    provincia = models.CharField(max_length=50, default='Córdoba')
    pais = models.CharField(max_length=50, default='Argentina')
    # Datos de Contrato
    disponible = models.BooleanField(default=True)
    alquiler_venta = models.CharField(max_length=15, choices=TIPO_TRANSACCION)
    precio_alquiler = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    precio_venta = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    # Caracteristicas
    baños = models.IntegerField(default=1)
    dormitorios = models.IntegerField(default=1)
    ambientes = models.IntegerField(default=1)
    cocheras = models.IntegerField(default=0, null=True, blank=True)
    metros_cubiertos = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    metros_descubiertos = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    metros_totales = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    pisos = models.IntegerField(default=1, null=True, blank=True)
    antiguedad = models.IntegerField(default=0, null=True, blank=True)
    piscina = models.BooleanField(default=False)
    # Movimientos
    creacion = models.DateTimeField(auto_now_add=True)
    ultima_actualizacion = models.DateTimeField(auto_now=True)


    # TODO: Define fields here

    class Meta:
        """Meta definition for Propiedad."""
        verbose_name = 'Propiedad'
        verbose_name_plural = 'Propiedades'

    def __str__(self):
        """Unicode representation of Propiedad."""
        return f'{self.denominacion}'
