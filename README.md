# SetteState - Sistema de Gestión Inmobiliaria

SetteState es un sistema completo de gestión inmobiliaria desarrollado con Django que permite administrar propiedades, contratos de alquiler, personas (propietarios e inquilinos) y facturación de manera eficiente.


## Características Principales

### Gestión de Propiedades
- Registro detallado de diferentes tipos de inmuebles (casas, departamentos, locales comerciales, etc.)
- Información completa: ubicación, características, precios, disponibilidad
- Asignación de propietarios a cada propiedad

### Gestión de Personas
- Base de datos de propietarios e inquilinos
- Información de contacto completa
- Validación de documentos y datos personales

### Administración de Contratos
- Creación y seguimiento de contratos de alquiler
- Actualizaciones automáticas de precios según frecuencia configurada (mensual, trimestral, etc.)
- Historial de actualizaciones de precios

### Sistema de Facturación
- Generación de facturas con múltiples conceptos (alquiler, expensas, servicios, etc.)
- Seguimiento del estado de las facturas (borrador, emitida, pagada, anulada)
- Exportación de facturas a PDF

### Información de Empresa
- Configuración de datos de la empresa para facturas y documentos


## Tecnologías Utilizadas
- **Backend:** Django 5.1 (Python)
- **Frontend:** Bootstrap 5
- **Base de Datos:** PostgreSQL
- **Formularios:** django-crispy-forms con Bootstrap 5
- **PDF:** Generación de documentos PDF
- **Configuración:** python-decouple para variables de entorno


## Estructura del Proyecto
El proyecto está organizado en varias aplicaciones Django:

- `persona`: Gestión de propietarios e inquilinos
- `propiedad`: Administración de inmuebles
- `contrato`: Gestión de contratos de alquiler
- `factura`: Sistema de facturación
- `empresa`: Configuración de datos de la empresa
- `imagen`: Gestión de imágenes para propiedades


## Modelos Principales

### Persona
- Información personal (nombre, apellido, documento)
- Datos de contacto (dirección, teléfono, email)
- Validación de documento y teléfono

### Propiedad
- Información básica (nombre, tipo, descripción)
- Ubicación (calle, número, ciudad, provincia)
- Características (baños, dormitorios, metros cuadrados, etc.)
- Precio y tipo de transacción (alquiler/venta)

### Contrato
- Vinculación entre inquilino y propiedad
- Fechas de inicio y fin
- Frecuencia de actualización de precios
- Historial de actualizaciones

### Factura
- Vinculación con contrato
- Estado (borrador, emitida, pagada, anulada)
- Múltiples conceptos (alquiler, expensas, servicios)
- Cálculo automático de totales


## Requisitos
- Python 3.8+
- PostgreSQL
- Dependencias listadas en `requirements.txt`


## Instalación

1. Clonar el repositorio:
   ```bash
   git clone https://github.com/tu-usuario/settestate.git
   cd settestate

2. Crear y activar un entorno virtual:
   ```bash
   python -m venv venv
   source venv/bin/activate # En Windows: venv/Scrip/activate

3. Instalar dependecias:
   ```bash
   pip install -r requirements.txt

4. Configurar variables de entorno:
   Crea un archivo .env en la raiz del proyecto con:
   ```
   DB_NAME=nombre_db
   DB_USER=usuario_db
   DB_PASSWORD=contraseña_db
   DB_HOST=localhost
   DB_PORT=5432

5. Aplica migraciones:
   ```bash
   python manage.py migrate

6. Crear superusuario:
   ```bash
   python manage.py createsuperuser

7. Ejecuta el servidor de desarrollo:
   ```bash
   python manage.py runserver


## Uso
- Acceder al panel de administración en `http://localhost:8000/admin`
- Crear propiedades, personas, contratos y facturas
- Gestionar actualizaciones de alquileres
- Generar facturas y exportarlas a PDF


## Características Futuras
- Dashboard con estadísticas y gráficos
- Sistema de notificaciones para vencimientos de contratos
- Integración con pasarelas de pago
- Portal para Inquilino
- Sistema de correo automatico para recordatorios de pago al inquilino


## Contribuciones
Las contribuciones y nuevas ideas son bienvenidas!!

1. Haz un fork del repositorio
2. Crea una rama para tu funcionalidad (git checkout -b feature/nueva-funcionalidad)
3. Realiza tus cambios y haz commit (git commit -m 'Añadir nueva funcionalidad')
4. Sube los cambios a tu fork (git push origin feature/nueva-funcionalidad)
5. Abre un Pull Request


## Licencia
MIT License

Copyright (c) [2025] [Gunsett Jeremias]

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.


## Contacto

- ✉️ Email: [jere.gunsett@gmail.com](jere.gunsett@gmail.com)
- 💼 LinkedIn: [Jeremias Gunsett](https://www.linkedin.com/in/jeremias-gunsett-b5316018b/)
- 🐱 GitHub: [@JereGun](https://github.com/JereGun)