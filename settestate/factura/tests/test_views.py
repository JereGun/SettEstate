from django.test import TestCase, Client
from django.utils import timezone
from django.urls import reverse
from django.contrib.auth.models import User
from decimal import Decimal
from factura.models import Factura, ItemFactura
from contrato.models import Contrato
from persona.models import Persona
from propiedad.models import Propiedad

class FacturaViewsTest(TestCase):
    def setUp(self):
        # Crear usuario para login
        self.user = User.objects.create_user(
            username='testuser',
            password='testpass123'
        )
        self.client = Client()
        self.client.login(username='testuser', password='testpass123')

        # Crear datos necesarios
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

    def test_lista_facturas(self):
        response = self.client.get(reverse('factura_list'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'factura/factura_list.html')
        self.assertContains(response, 'TEST-001')

    def test_detalle_factura(self):
        response = self.client.get(
            reverse('factura_detail', kwargs={'pk': self.factura.pk})
        )
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'factura/factura_detail.html')

    def test_crear_factura(self):
        data = {
            'contrato': self.contrato.id,
            'fecha_vencimiento': timezone.now().date() + timezone.timedelta(days=10),
            'estado': 'BORRADOR'
        }
        response = self.client.post(reverse('factura_create'), data)
        self.assertEqual(response.status_code, 302)  # Redirección después de crear

    def test_crear_item_factura(self):
        data = {
            'descripcion': 'Test Item',
            'monto': '100.00',
            'tipo': 'SERVICIO'
        }
        response = self.client.post(
            reverse('itemfactura_create', kwargs={'factura_id': self.factura.pk}),
            data
        )
        self.assertEqual(response.status_code, 302)
        self.assertTrue(
            ItemFactura.objects.filter(factura=self.factura, descripcion='Test Item').exists()
        )
