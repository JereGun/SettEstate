from django.db import models
from django.core.validators import MinValueValidator
from decimal import Decimal

class Factura(models.Model):
    ESTADO_CHOICES = [
        ('BORRADOR', 'Borrador'),
        ('EMITIDA', 'Emitida'),
        ('ANULADA', 'Anulada'),
        ('PAGADA', 'Pagada'),
    ]

    """Model definition for Factura."""
    numero = models.CharField(max_length=20, unique=True)
    contrato = models.ForeignKey('contrato.Contrato', on_delete=models.PROTECT)
    fecha_emision = models.DateField()
    fecha_vencimiento = models.DateField()
    estado = models.CharField(max_length=10, choices=ESTADO_CHOICES, default='BORRADOR')
    total = models.DecimalField(max_digits=10, decimal_places=2, validators=[MinValueValidator(Decimal('0.00'))], default=Decimal('0.00'))
    creacion = models.DateTimeField(auto_now_add=True)
    modificacion = models.DateTimeField(auto_now=True)

    # TODO: Define fields here

    class Meta:
        """Meta definition for Factura."""
        verbose_name = 'Factura'
        verbose_name_plural = 'Facturas'

    def calcular_total(self):
        """Calcula el total sumando todos los items de la factura"""
        self.total = self.items.aggregate(
            total=models.Sum('subtotal')
        )['total'] or Decimal('0.00')
        self.save()
        return self.total

    def es_editable(self):
        """Determina si la factura es editable"""
        return self.estado == "BORRADOR"
    
    def emitir(self):
        """Cambia el estado a EMITIDA"""
        if self.estado == "BORRADOR":
            self.estado = "EMITIDA"
            self.save()
    
    def anular(self):
        """Cancela la Factura"""
        if self.estado in ['BORRADOR', 'EMITIDA']:
            self.estado = 'ANULADA'
            self.save()

    def marcar_pagada(self):
        """Marca la factura como pagada"""
        if self.estado == 'EMITIDA':
            self.estado = 'PAGADA'
            self.save()
    def marcar_borrador(self):
        if self.estado in ['EMITIDA', 'PAGADA', 'ANULADA']:
            self.estado = 'BORRADOR'
            self.save()

    def __str__(self):
        return f"Factura {self.numero} - {self.contrato}"

class ItemFactura(models.Model):
    TIPO_CHOICES = [
        ('ALQUILER', 'Alquiler'),
        ('EXPENSAS', 'Expensas'),
        ('SERVICIO', 'Servicio'),
        ('IMPUESTO', 'Impuesto'),
        ('OTRO', 'Otro'),
    ]
    """Model definition for ItemFactura."""
    factura = models.ForeignKey(Factura, on_delete=models.CASCADE, related_name='items')
    tipo = models.CharField(max_length=10, choices=TIPO_CHOICES)
    descripcion = models.CharField(max_length=100)
    monto = models.DecimalField(max_digits=10, decimal_places=2, validators=[MinValueValidator(Decimal('0.00'))])
    subtotal = models.DecimalField(max_digits=10, decimal_places=2, validators=[MinValueValidator(Decimal('0.00'))])

    # TODO: Define fields here

    class Meta:
        """Meta definition for ItemFactura."""
        verbose_name = 'ItemFactura'
        verbose_name_plural = 'ItemFacturas'

    def save(self, *args, **kwargs):
        self.subtotal = self.monto
        super().save(*args, **kwargs)
        self.factura.calcular_total()

    def __str__(self):
        return f"{self.descripcion} - {self.monto}"
    
        

