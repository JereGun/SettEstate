from django.test import TestCase
from datetime import date
from .models import Persona

class PersonaModelTest(TestCase):
    def test_crear_persona(self):
        persona = Persona.objects.create(
            documento='123456789',
            nombre='Juan',
            apellido='Perez',
            fecha_nacimiento=date(1980, 1, 1),
            direccion='Calle Falsa 123',
            ciudad='Ciudad Falsa',
            provincia='Provincia Falsa',
            pais='Pais Falso',
            telefono='1234567890',
            email='email@falso.com')
        
        self.assertEqual(persona.documento, '123456789')
        self.assertEqual(persona.nombre, 'Juan')
        self.assertEqual(persona.apellido, 'Perez')
        self.assertEqual(persona.fecha_nacimiento, date(1980, 1, 1))
        self.assertEqual(persona.direccion, 'Calle Falsa 123')
        self.assertEqual(persona.ciudad, 'Ciudad Falsa')
        self.assertEqual(persona.provincia, 'Provincia Falsa')
        self.assertEqual(persona.pais, 'Pais Falso')
        self.assertEqual(persona.telefono, '1234567890')
        self.assertEqual(persona.email, 'email@falso.com')

    def test_documento_unico(self):
        persona = Persona.objects.create(
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
        with self.assertRaises(Exception):
            Persona.objects.create(
                documento='123456789',
                nombre='Ana',
                apellido='Gerbacia',
                fecha_nacimiento=date(1990, 10, 1),
                direccion='Calle no tan falsa 1234',
                ciudad='Ciudad Falsa',
                provincia='Provincia Falsa',
                pais='Pais Falso',
                telefono='1234567890',
        )
        
    def test_documento_invalido(self):
        with self.assertRaises(Exception):
            Persona.objects.create(
                documento='12345ABC',
                nombre='Juan',
                apellido='Perez',
                fecha_nacimiento=date(1980, 1, 1),
                direccion='Calle Falsa 123',
                ciudad='Ciudad Falsa',
                provincia='Provincia Falsa',
                pais='Pais Falso',
                telefono='1234567890',
            )