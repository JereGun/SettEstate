from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils import timezone
from contrato.models import Contrato
from .models import Factura, ItemFactura
from decimal import Decimal


@receiver(post_save, sender=Contrato)
def crear_factura_inicial(sender, instance, created, **kwargs):
    """
    Crea la primera factura cuando se crea un contrato nuevo
    """
    if created:
        hoy = timezone.now().date()
        # Crear la factura inicial
        factura = Factura.objects.create(
            numero=f"B-{hoy.strftime('%Y%m')}-{instance.id}",
            contrato=instance,
            fecha_emision=hoy,
            fecha_vencimiento=hoy.replace(day=1) + timezone.timedelta(days=32),
            total=Decimal('0.00')
        )

        # Crear el ítem de alquiler
        ItemFactura.objects.create(
            factura=factura,
            tipo='ALQUILER',
            descripcion=f'Alquiler {hoy.strftime("%B %Y")}',
            monto=instance.get_monto_alquiler()
        )