from django.db import models
from persona.models import Persona
from django.core.exceptions import ValidationError

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
    descripcion = models.TextField()
    tipo = models.CharField(max_length=20, choices=TIPOS)
    disponible = models.BooleanField(default=True)
    alquiler_venta = models.CharField(max_length=15, choices=TIPO_TRANSACCION)
    precio = models.DecimalField(max_digits=10, decimal_places=2)
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

class Atributo(models.Model):
    TIPO_DATO = [
        ('TEXTO', 'Texto'),
        ('NUMERICO', 'Numérico'),
        ('BOOLEANO', 'Booleano'),
    ]
    """Model definition for Atributo."""
    nombre = models.CharField(max_length=50)
    tipo_dato = models.CharField(max_length=10, choices=TIPO_DATO)


    # TODO: Define fields here

    class Meta:
        """Meta definition for Atributo."""
        verbose_name = 'Atributo'
        verbose_name_plural = 'Atributos'

    def __str__(self):
        """Unicode representation of Atributo."""
        return f'{self.nombre} - {self.tipo_dato}'

class ValorAtributo(models.Model):
    """Model definition for ValorAtributo."""
    atributo = models.ForeignKey(Atributo, on_delete=models.CASCADE)
    propiedad = models.ForeignKey(Propiedad, on_delete=models.CASCADE)
    valor = models.CharField(max_length=100)

    # TODO: Define fields here

    def __str__(self):
        """Unicode representation of ValorAtributo."""
        return f'{self.atributo.nombre}: {self.valor}'
    
    def clean(self):
        super().clean()

        if self.atributo.tipo_dato == 'TEXTO':
            pass
        elif self.atributo.tipo_dato == 'NUMERICO':
            try:
                int(self.valor)
            except ValueError:
                raise ValidationError('El valor debe ser numerico')
        elif self.atributo.tipo_dato == 'BOOLEANO':
            if self.valor.lower() not in ['true', 'false', 1, 0, 'Si', 'No']:
                raise ValidationError('El valor debe ser booleano')

