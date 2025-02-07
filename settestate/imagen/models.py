from django.db import models
from django.core.exceptions import ValidationError
from imagekit.models import ProcessedImageField
from imagekit.processors import ResizeToFill
from propiedad.models import Propiedad
import os
from django.db.models.signals import post_delete
from django.dispatch import receiver

def upload_to_propiedad(instance, filename):
    return f'media/imagenes_propiedades/{instance.propiedad.id}/{filename}'

class ImagenPropiedad(models.Model):
    propiedad = models.ForeignKey(Propiedad, on_delete=models.CASCADE)
    imagen = ProcessedImageField(
        upload_to=upload_to_propiedad,
        processors=[ResizeToFill(800, 600)],
        format='JPEG',
        options={'quality': 80}
    )
    portada = models.BooleanField(default=False)

    class Meta:
        verbose_name = 'Imagen'
        verbose_name_plural = 'Imagenes'

    def clean(self):
        if self.portada:
            query = ImagenPropiedad.objects.filter(propiedad=self.propiedad, portada=True)
            if self.pk:
                query = query.exclude(pk=self.pk)
            if query.exists():
                raise ValidationError('Ya existe una imagen marcada como portada para esta propiedad')

    def save(self, *args, **kwargs):
        self.clean()
        super().save(*args, **kwargs)

@receiver(post_delete, sender=ImagenPropiedad)
def eliminar_imagen(sender, instance, **kwargs):
    if instance.imagen:
        if os.path.isfile(instance.imagen.path):
            os.remove(instance.imagen.path)