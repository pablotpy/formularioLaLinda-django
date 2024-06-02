import sys
from django.db import models, IntegrityError
from django.core.exceptions import ValidationError
from django.core.validators import RegexValidator
from PIL import Image
from io import BytesIO
from django.core.files.uploadedfile import InMemoryUploadedFile


class FormularioConcurso(models.Model):
    nombres = models.CharField(max_length=50)
    apellidos = models.CharField(max_length=50, validators=[RegexValidator(regex='^[a-zA-ZñÑ ]*$', message='Apellido Inválido')])
    ci = models.CharField(max_length=10)
    telefono = models.CharField(max_length=12)
    correo = models.EmailField()
    nrocomprobante = models.CharField(max_length=15, unique=True , error_messages={'unique':"Este numero de comprobante ya ha sido registrado."}) 
    imagen = models.ImageField(upload_to='imagenes/')

    def save(self, *args, **kwargs):
        if not self.id:
            self.imagen = self.compressImage(self.imagen)
        super(FormularioConcurso, self).save(*args, **kwargs)
    def compressImage(self,imagen):
        imageTemproary = Image.open(imagen)
        outputIoStream = BytesIO()
        imageTemproaryResized = imageTemproary.resize( (1020,573) ) 
        imageTemproary.save(outputIoStream , format='JPEG', quality=60)
        outputIoStream.seek(0)
        imagen = InMemoryUploadedFile(outputIoStream,'ImageField', "%s.jpg" % imagen.name.split('.')[0], 'image/jpeg', sys.getsizeof(outputIoStream), None)
        return imagen






