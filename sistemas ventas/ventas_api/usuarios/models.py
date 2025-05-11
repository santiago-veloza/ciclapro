from django.db import models

# Create your models here.
class Usuario(models.Model):
    username = models.CharField(max_length=100, unique=True)
    apellido = models.CharField(max_length=100)
    rol = models.CharField(max_length=50)
    fecha_nacimiento = models.DateField()
    correo_electronico = models.EmailField(unique=True)
    telefono = models.CharField(max_length=15, unique=True)
    direccion = models.CharField(max_length=255)
    fecha_registro = models.DateTimeField(auto_now_add=True)
    Contraseña = models.CharField(max_length=100, default='123456')


    def __str__(self):
        return self.username
