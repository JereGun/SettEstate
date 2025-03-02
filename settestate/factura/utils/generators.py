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
    
    # Obtener contratos activos
    contratos_activos = Contrato.objects.filter(
        fecha_inicio__lte=hoy,
        fecha_fin__gte=hoy
    )

    facturas_generadas = []
    
    for contrato in contratos_activos:
        # Verificar si ya existe una factura para este mes y contrato
        factura_existente = Factura.objects.filter(
            contrato=contrato,
            fecha_emision__year=hoy.year,
            fecha_emision__month=hoy.month
        ).first()
        
        if not factura_existente:
            # Generar numero de factura
            ultimo_numero = Factura.objects.order_by('-numero').first()
            nuevo_numero = f"FAC-{str(int(ultimo_numero.numero.split('-')[1]) + 1).zfill(8)}" if ultimo_numero else "FAC-00000001"

            # Crear la factura
            factura = Factura.objects.create(
                numero=nuevo_numero,
                contrato=contrato,
                fecha_emision=hoy,
                fecha_vencimiento=primer_dia_mes_siguiente,
                estado='BORRADOR',  # Agregar estado inicial
                total=Decimal('0.00')
            )

            # Crear el ítem de alquiler
            ItemFactura.objects.create(
                factura=factura,
                tipo='ALQUILER',
                descripcion=f'Alquiler {hoy.strftime("%B %Y")}',
                monto=contrato.get_monto_alquiler()
            )
            
            # Actualizar el total de la factura
            factura.total = factura.calcular_total()
            factura.save()
            
            facturas_generadas.append(factura)
    
    return facturas_generadas
