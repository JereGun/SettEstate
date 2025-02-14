from django.test import TestCase
from django.utils import timezone
from decimal import Decimal
from factura.utils.generators import generar_factura_mensual
from factura.models import Factura, ItemFactura
from contrato.models import Contrato
from persona.models import Persona
from propiedad.models import Propiedad

class GeneradoresFacturaTest(TestCase):
    def setUp(self):
        # Crear datos necesarios
        self.persona = Persona.objects.create(
            nombre="Juan",
            apellido="Pérez",
            documento="12345678"
        )
        
        self.propiedad = Propiedad.objects.create(
            nombre="Casa Test",
            direccion="Calle Test 123",
            precio_alquiler=Decimal('1000.00')
        )
        
        self.contrato = Contrato.objects.create(
            inquilino=self.persona,
            propiedad=self.propiedad,
            fecha_inicio=timezone.now().date(),
            fecha_fin=timezone.now().date() + timezone.timedelta(days=365),
            frecuencia_actualizacion='MENSUAL'
        )

    def test_generar_factura_mensual(self):
        # Verificar que no hay facturas inicialmente
        self.assertEqual(Factura.objects.count(), 0)

        # Generar facturas
        facturas = generar_factura_mensual()

        # Verificar que se creó una factura
        self.assertEqual(len(facturas), 1)
        self.assertEqual(Factura.objects.count(), 1)

        # Verificar que la factura tiene el ítem de alquiler
        factura = Factura.objects.first()
        self.assertTrue(
            ItemFactura.objects.filter(
                factura=factura,
                tipo='ALQUILER'
            ).exists()
        )

    def test_no_duplicar_facturas(self):
        # Generar facturas por primera vez
        facturas_1 = generar_factura_mensual()
        
        # Intentar generar facturas nuevamente en el mismo mes
        facturas_2 = generar_factura_mensual()

        # Verificar que no se crearon facturas duplicadas
        self.assertEqual(len(facturas_1), 1)
        self.assertEqual(len(facturas_2), 0)
        self.assertEqual(Factura.objects.count(), 1)
