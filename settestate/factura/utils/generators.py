# factura/utils/generators.py
from django.utils import timezone
from datetime import timedelta
from decimal import Decimal
from contrato.models import Contrato
from ..models import Factura, ItemFactura

def generar_factura_mensual():
    """
    Genera las facturas mensuales para todos los contratos activos
    """
    hoy = timezone.now().date()
    primer_dia_mes_siguiente = (hoy.replace(day=1) + timedelta(days=32)).replace(day=1)
    
    contratos_activos = Contrato.objects.filter(
        fecha_inicio__lte=hoy,
        fecha_fin__gte=hoy
    )

    facturas_generadas = []
    for contrato in contratos_activos:
        # Verificar si ya existe una factura para este mes
        if not Factura.objects.filter(
            contrato=contrato,
            fecha_emision__year=hoy.year,
            fecha_emision__month=hoy.month
        ).exists():
            # Crear la factura
            factura = Factura.objects.create(
                numero=f"B-{hoy.strftime('%Y%m')}-{contrato.id}",
                contrato=contrato,
                fecha_emision=hoy,
                fecha_vencimiento=primer_dia_mes_siguiente,
                total=Decimal('0.00')
            )

            # Crear el ítem de alquiler
            ItemFactura.objects.create(
                factura=factura,
                tipo='ALQUILER',
                descripcion=f'Alquiler {hoy.strftime("%B %Y")}',
                monto=contrato.get_monto_alquiler_vigente()
            )
            
            facturas_generadas.append(factura)
    
    return facturas_generadas
