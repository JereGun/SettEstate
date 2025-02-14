from django_cron import CronJobBase, Schedule
from .utils.generators import generar_factura_mensual

class GenerarFacturasMensualesCronJob(CronJobBase):
    RUN_AT_TIMES = ['00:00']  # Se ejecutará a la medianoche

    schedule = Schedule(run_at_times=RUN_AT_TIMES)
    code = 'factura.generar_facturas_mensuales'

    def do(self):
        facturas = generar_factura_mensual()
        return f"Se generaron {len(facturas)} facturas"
