from django.shortcuts import render, redirect
from .forms import TuFormulario
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.utils.html import strip_tags

def formulario(request):
    if request.method == 'POST':
        form = TuFormulario(request.POST, request.FILES)
        if form.is_valid():
            nombres = form.cleaned_data.get("nombres")
            apellidos = form.cleaned_data.get("apellidos")
            correo = form.cleaned_data.get("correo")
            
            # Guardar el formulario en la base de datos
            form.save()
            
            # Enviar correo electrónico de confirmación
            subject = "Confirmación de registro"
            html_message = render_to_string('correo_confirmacion.html', {'nombres': nombres, 'apellidos': apellidos})
            plain_message = strip_tags(html_message)
            send_mail(subject, plain_message, 'llalindavinospy@gmail.com', [correo], html_message=html_message)
            
            # Establecer una marca en la sesión para indicar que el formulario se ha completado con éxito
            request.session['formulario_completado'] = True
            return redirect('registro_exitoso')  # Redirecciona a la página de éxito
    else:
        form = TuFormulario()
    return render(request, 'formulario.html', {'form': form})

def registro_exitoso(request):
    if request.session.get('formulario_completado'):
        # Eliminar la marca de que el formulario se ha completado para evitar que se acceda nuevamente
        del request.session['formulario_completado']
        return render(request, 'registro_exitoso.html')
    else:
        return redirect('formulario')  # Si el formulario no se ha completado, redirecciona de nuevo al formulario
