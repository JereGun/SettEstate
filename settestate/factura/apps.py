from django.apps import AppConfig

class FacturaConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'factura'

    def ready(self):
        import factura.signals