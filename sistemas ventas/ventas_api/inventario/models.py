from django.db import models
from productos.models import Producto  


class Inventario(models.Model):
    id_inventario = models.AutoField(primary_key=True)
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    marca = models.CharField(max_length=100, default='generica')
    cantidad = models.IntegerField()

    def __str__(self):
        return f"{self.marca} - {self.producto} ({self.cantidad})"
