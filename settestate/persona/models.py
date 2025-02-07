from django.db import models
from django.core.validators import RegexValidator

class Persona(models.Model):
    """Model definition for Persona."""
    documento = models.CharField(max_length=9, 
                                 unique=True, 
                                 primary_key=True, 
                                 validators=[
                                     RegexValidator(regex='^[0-9]*$',
                                                   message='El documento debe tener 9 caracteres')])
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    fecha_nacimiento = models.DateField()
    direccion = models.CharField(max_length=100)
    ciudad = models.CharField(max_length=50)
    provincia = models.CharField(max_length=50)
    pais = models.CharField(max_length=50)
    telefono = models.CharField(max_length=20, 
                                validators=[
                                    RegexValidator(regex='^[0-9]*$',
                                                   message='El teléfono debe tener solo números')])
    email = models.EmailField(max_length=100)
    creacion = models.DateTimeField(auto_now_add=True)
    ultima_actualizacion = models.DateTimeField(auto_now=True)

    # TODO: Define fields here

    class Meta:
        """Meta definition for Persona."""

        verbose_name = 'Persona'
        verbose_name_plural = 'Personas'

    def __str__(self):
        """Unicode representation of Persona."""
        return f'{self.nombre} {self.apellido}'
    
    def nombre_completo(self):
        return f'{self.nombre} {self.apellido}'