from django.test import TestCase
from django.utils import timezone
from decimal import Decimal
from datetime import date
from factura.models import Factura, ItemFactura
from contrato.models import Contrato
from persona.models import Persona
from propiedad.models import Propiedad

class SignalsTest(TestCase):
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

    def test_crear_factura_al_crear_contrato(self):
        # Verificar que no hay facturas inicialmente
        self.assertEqual(Factura.objects.count(), 0)

        # Crear un nuevo contrato
        contrato = Contrato.objects.create(
            inquilino=self.persona,
            propiedad=self.propiedad,
            fecha_inicio=timezone.now().date(),
            fecha_fin=timezone.now().date() + timezone.timedelta(days=365),
            frecuencia_actualizacion='MENSUAL'
        )

        # Verificar que se creó una factura automáticamente
        self.assertEqual(Factura.objects.count(), 1)
        
        # Verificar que la factura tiene el ítem de alquiler
        factura = Factura.objects.first()
        self.assertTrue(
            ItemFactura.objects.filter(
                factura=factura,
                tipo='ALQUILER'
            ).exists()
        )
