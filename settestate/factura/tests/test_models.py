from django.test import TestCase
from django.utils import timezone
from datetime import date
from decimal import Decimal
from factura.models import Factura, ItemFactura
from contrato.models import Contrato
from persona.models import Persona
from propiedad.models import Propiedad

class FacturaModelTest(TestCase):
    def setUp(self):
        # Crear datos necesarios para las pruebas
        self.persona = Persona.objects.create(
            documento='123456789',
            nombre='Juan',
            apellido='Perez',
            fecha_nacimiento=date(1980, 1, 1),
            direccion='Calle Falsa 123',
            ciudad='Ciudad Falsa',
            provincia='Provincia Falsa',
            pais='Pais Falso',
            telefono='1234567890',
            email='email@falso.com'
        )
        
        self.propiedad = Propiedad.objects.create(
            nombre='Casa en el centro',
            calle='Av. Siempre Viva 123',
            dueño=self.persona,
            numeracion='123',
            piso='1',
            departamento='A',
            ciudad='Córdoba',
            provincia='Córdoba',
            pais='Argentina',
            descripcion='Una casa muy bonita en el centro de la ciudad.',
            tipo='CASA',
            disponible=True,
            alquiler_venta='VENTA',
            precio=100000.00,
            baños=2,
            dormitorios=3,
            habitaciones=4,
            cocheras=1,
            metros_cuadrados=150.00,
            pisos=2,
            antiguedad=10,
            piscina=True
        )
        
        self.contrato = Contrato.objects.create(
            inquilino=self.persona,
            propiedad=self.propiedad,
            fecha_inicio=timezone.now().date(),
            fecha_fin=timezone.now().date() + timezone.timedelta(days=365),
            frecuencia_actualizacion='MENSUAL'
        )

        self.factura = Factura.objects.create(
            numero="TEST-001",
            contrato=self.contrato,
            fecha_emision=timezone.now().date(),
            fecha_vencimiento=timezone.now().date() + timezone.timedelta(days=10),
            total=Decimal('0.00')
        )

    def test_crear_factura(self):
        self.assertEqual(self.factura.estado, 'BORRADOR')
        self.assertEqual(self.factura.total, Decimal('0.00'))

    def test_calcular_total(self):
        # Crear items de factura
        ItemFactura.objects.create(
            factura=self.factura,
            tipo='ALQUILER',
            descripcion='Alquiler Enero 2024',
            monto=Decimal('1000.00')
        )
        ItemFactura.objects.create(
            factura=self.factura,
            tipo='SERVICIO',
            descripcion='Expensas',
            monto=Decimal('200.00')
        )

        # Verificar que el total se calculó correctamente
        self.assertEqual(self.factura.total, Decimal('1200.00'))

