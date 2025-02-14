from django.test import TestCase
from datetime import date
from persona.models import Persona
from propiedad.models import Propiedad

class PropiedadModelTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        # Crear una persona para usarla como dueño de la propiedad
        cls.dueño = Persona.objects.create(
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
        
        # Crear una propiedad para las pruebas
        cls.propiedad = Propiedad.objects.create(
            nombre='Casa en el centro',
            calle='Av. Siempre Viva 123',
            dueño=cls.dueño,
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

    def test_nombre_label(self):
        propiedad = Propiedad.objects.get(id=1)
        field_label = propiedad._meta.get_field('nombre').verbose_name
        self.assertEqual(field_label, 'nombre')

    def test_calle_label(self):
        propiedad = Propiedad.objects.get(id=1)
        field_label = propiedad._meta.get_field('calle').verbose_name
        self.assertEqual(field_label, 'calle')

    def test_dueño_label(self):
        propiedad = Propiedad.objects.get(id=1)
        field_label = propiedad._meta.get_field('dueño').verbose_name
        self.assertEqual(field_label, 'dueño')

    def test_nombre_max_length(self):
        propiedad = Propiedad.objects.get(id=1)
        max_length = propiedad._meta.get_field('nombre').max_length
        self.assertEqual(max_length, 50)

    def test_calle_max_length(self):
        propiedad = Propiedad.objects.get(id=1)
        max_length = propiedad._meta.get_field('calle').max_length
        self.assertEqual(max_length, 100)

    def test_tipo_max_length(self):
        propiedad = Propiedad.objects.get(id=1)
        max_length = propiedad._meta.get_field('tipo').max_length
        self.assertEqual(max_length, 20)

    def test_alquiler_venta_max_length(self):
        propiedad = Propiedad.objects.get(id=1)
        max_length = propiedad._meta.get_field('alquiler_venta').max_length
        self.assertEqual(max_length, 15)

    def test_precio_max_digits(self):
        propiedad = Propiedad.objects.get(id=1)
        max_digits = propiedad._meta.get_field('precio').max_digits
        self.assertEqual(max_digits, 10)

    def test_precio_decimal_places(self):
        propiedad = Propiedad.objects.get(id=1)
        decimal_places = propiedad._meta.get_field('precio').decimal_places
        self.assertEqual(decimal_places, 2)

    def test_metodos_str(self):
        propiedad = Propiedad.objects.get(id=1)
        expected_object_name = f'{propiedad.nombre} - {propiedad.tipo} - {propiedad.alquiler_venta} - ${propiedad.precio}'
        self.assertEqual(str(propiedad), expected_object_name)

    def test_propiedad_creacion(self):
        propiedad = Propiedad.objects.get(id=1)
        self.assertIsNotNone(propiedad.creacion)

    def test_propiedad_ultima_actualizacion(self):
        propiedad = Propiedad.objects.get(id=1)
        self.assertIsNotNone(propiedad.ultima_actualizacion)

    def test_propiedad_disponible_default(self):
        propiedad = Propiedad.objects.get(id=1)
        self.assertTrue(propiedad.disponible)

    def test_propiedad_piscina_default(self):
        propiedad = Propiedad.objects.get(id=1)
        self.assertTrue(propiedad.piscina)

    def test_propiedad_ciudad_default(self):
        propiedad = Propiedad.objects.get(id=1)
        self.assertEqual(propiedad.ciudad, 'Córdoba')

    def test_propiedad_provincia_default(self):
        propiedad = Propiedad.objects.get(id=1)
        self.assertEqual(propiedad.provincia, 'Córdoba')

    def test_propiedad_pais_default(self):
        propiedad = Propiedad.objects.get(id=1)
        self.assertEqual(propiedad.pais, 'Argentina')

    def test_propiedad_baños_default(self):
        propiedad = Propiedad.objects.get(id=1)
        self.assertEqual(propiedad.baños, 2)

    def test_propiedad_dormitorios_default(self):
        propiedad = Propiedad.objects.get(id=1)
        self.assertEqual(propiedad.dormitorios, 3)

    def test_propiedad_habitaciones_default(self):
        propiedad = Propiedad.objects.get(id=1)
        self.assertEqual(propiedad.habitaciones, 4)

    def test_propiedad_cocheras_default(self):
        propiedad = Propiedad.objects.get(id=1)
        self.assertEqual(propiedad.cocheras, 1)

    def test_propiedad_metros_cuadrados_default(self):
        propiedad = Propiedad.objects.get(id=1)
        self.assertEqual(propiedad.metros_cuadrados, 150.00)

    def test_propiedad_pisos_default(self):
        propiedad = Propiedad.objects.get(id=1)
        self.assertEqual(propiedad.pisos, 2)

    def test_propiedad_antiguedad_default(self):
        propiedad = Propiedad.objects.get(id=1)
        self.assertEqual(propiedad.antiguedad, 10)