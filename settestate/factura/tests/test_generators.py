from django.test import TestCase
from django.utils import timezone
from datetime import date
from decimal import Decimal
from factura.utils.generators import generar_factura_mensual
from factura.models import Factura, ItemFactura
from contrato.models import Contrato
from persona.models import Persona
from propiedad.models import Propiedad

class GeneradoresFacturaTest(TestCase):
    def setUp(self):
        print("Inicio setUp")
        print(f"Facturas antes de limpiar: {Factura.objects.count()}")
        # Limpiar todas las facturas existentes
        Factura.objects.all().delete()
        Contrato.objects.all().delete()
        ItemFactura.objects.all().delete()
        print(f"Facturas despues de limpiar: {Factura.objects.count()}")

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

    def test_generar_factura_mensual(self):
        # Verificar estado inicial
        self.assertEqual(Factura.objects.count(), 0)
        self.assertEqual(ItemFactura.objects.count(), 0)
        
        # Asegurarse de que el contrato tiene monto de alquiler
        self.contrato.monto_alquiler = Decimal('1000.00')
        self.contrato.save()

        # Generar facturas
        facturas = generar_factura_mensual()

        # Verificaciones
        self.assertEqual(len(facturas), 1, "Debería generarse exactamente una factura")
        self.assertEqual(Factura.objects.count(), 1, "Debería haber exactamente una factura en la base de datos")
        self.assertEqual(ItemFactura.objects.count(), 1, "Debería haber exactamente un ítem de factura")

    def test_no_duplicar_facturas(self):
        # Asegurarse de que el contrato tiene monto de alquiler
        self.contrato.monto_alquiler = Decimal('1000.00')
        self.contrato.save()

        # Verificar estado inicial
        self.assertEqual(Factura.objects.count(), 0)
        
        # Primera generación
        facturas_1 = generar_factura_mensual()
        self.assertEqual(len(facturas_1), 1, "Primera generación debería crear una factura")
        
        # Segunda generación
        facturas_2 = generar_factura_mensual()
        self.assertEqual(len(facturas_2), 0, "Segunda generación no debería crear facturas")
        
        # Verificación final
        self.assertEqual(Factura.objects.count(), 1, "Debería haber exactamente una factura en total")