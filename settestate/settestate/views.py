from django.views.generic import TemplateView
from django.shortcuts import render, redirect
from django.core.mail import send_mail

class IndexView(TemplateView):
    template_name = 'index.html'

class ContactoView(TemplateView):
    template_name = 'contacto.html'

def enviar_contacto(request):
    if request.method == 'POST':
        nombre = request.POST['nombre']
        email = request.POST['email']
        mensaje = request.POST['mensaje']
        
        # Configuracion de envio de mails
        send_mail(
            f'Mensaje de {nombre}',
            mensaje,
            email,
            ['tu_correo@example.com'],  
        )
        return redirect('index')  
    return redirect('contacto')  
