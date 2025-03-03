from io import BytesIO
from django.http import HttpResponse
from django.template.loader import get_template
from xhtml2pdf import pisa
from django.conf import settings
import os
from django.contrib.staticfiles import finders  # Añade esta importación que faltaba

def link_callback(uri, rel):
    """
    Convierte las URLs de HTML en rutas absolutas del sistema de archivos para que
    xhtml2pdf pueda acceder a los archivos estáticos y de medios
    """
    # Si la URI es una URL absoluta (comienza con http o https), la devolvemos tal cual
    if uri.startswith('http://') or uri.startswith('https://'):
        return uri

    # Convertir la URI a una ruta del sistema de archivos
    if uri.startswith('/static/'):
        path = finders.find(uri.replace('/static/', ''))
        if path:
            return path
        else:
            # Si no se encuentra en static, devolver una cadena vacía o una ruta por defecto
            return ""  # Devolver cadena vacía en lugar de None
    
    elif uri.startswith('/media/'):
        # Ruta absoluta al directorio de medios
        media_root = settings.MEDIA_ROOT
        # Eliminar '/media/' del inicio de la URI para obtener la ruta relativa
        relative_path = uri.replace('/media/', '')
        path = os.path.join(media_root, relative_path)
        
        # Verificar si el archivo existe
        if os.path.isfile(path):
            return path
        else:
            # Si no se encuentra el archivo, podemos usar un logo por defecto o devolver una cadena vacía
            print(f"Archivo no encontrado: {path}")
            # Opcionalmente, devolver un logo por defecto
            if hasattr(settings, 'STATIC_ROOT'):
                default_logo = os.path.join(settings.STATIC_ROOT, 'img/default_logo.png')
                if os.path.isfile(default_logo):
                    return default_logo
            
            # Si no hay logo por defecto, devolver una cadena vacía
            return ""  # Devolver cadena vacía en lugar de None
    
    # Si no es una URI de static o media, devolver la URI original
    return uri

def render_to_pdf(template_src, context_dict={}):
    """
    Renderiza un template HTML a un archivo PDF
    """
    template = get_template(template_src)
    html = template.render(context_dict)
    result = BytesIO()
    
    # Crear el PDF usando el link_callback para manejar imágenes
    pdf = pisa.pisaDocument(
        BytesIO(html.encode("UTF-8")), 
        result,
        encoding='UTF-8',
        link_callback=link_callback
    )
    
    if not pdf.err:
        return result.getvalue()
    return None
