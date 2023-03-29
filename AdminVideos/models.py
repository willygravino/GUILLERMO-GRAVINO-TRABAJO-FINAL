from django.db import models
from django.contrib.auth.models import User

    #https://www.geeksforgeeks.org/urlfield-django-models/#field-options
    #models.URLField(max_length=200, **options)

#from django.db import models
#from django.db.models import Model
# Create your models here.
  
#class GeeksModel(Model):
   # geeks_field = models.URLField(max_length = 200)


class Video(models.Model):
    nombre_video = models.CharField(max_length=30)
    url_video = models.CharField(max_length=80, blank=False)
    descripcion_video = models.CharField(max_length=300)
    quienes_aparecen = models.CharField('Ingrese el nombre y apellido de quienes participan en el video, separados por coma', max_length=120, blank=False)
    propietario = models.ForeignKey(to=User, on_delete=models.CASCADE, related_name="propietario")
    image = models.ImageField(upload_to="videos/", null=True, blank=True)
    fecha_video= models.DateTimeField()

    @property
    def image_url(self):
        return self.image.url if self.image else '/media/videos/nuestrotubo.png'

    def __str__(self):
        return f"{self.id} - {self.nombre_video}"
    
    
class Profile(models.Model):
     user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="profile")
     nombre_completo = models.CharField(max_length=80, blank=False)
     avatar = models.ImageField(upload_to="avatares", null=True, blank=True)

     @property
     def avatar_url(self):
        return self.avatar.url if self.avatar else '/media/avatares/default-avatar.png'
     

     

class Mensaje(models.Model):
    mensaje = models.TextField(max_length=1000)
    email = models.EmailField()
    creado_el = models.DateTimeField(auto_now_add=True) 
    destinatario = models.ForeignKey(User, on_delete=models.CASCADE, related_name="mensajes")


