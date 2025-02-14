from django.test import TestCase
from django.utils import timezone
from decimal import Decimal
from factura.models import Factura, ItemFactura
from contrato.models import Contrato
from persona.models import Persona
from propiedad.models import Propiedad

class SignalsTest(TestCase):
    def setUp(self):
        self.persona = Persona.objects.create(
            nombre="Juan",
            apellido="Pérez",
            dni="12345678"
        )
        
        self.propiedad = Propiedad.objects.create(
            nombre="Casa Test",
            direccion="Calle Test 123",
            precio_alquiler=Decimal('1000.00')
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
