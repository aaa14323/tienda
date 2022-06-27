from django.db import models

# Create your models here.

#muchos producto tiene muchos cliets
class Producto(models.Model):
    nombre = models.CharField(max_length=15)
    precio = models.IntegerField(null=True)
    imagen = models.ImageField(upload_to='images/', null=True)

    def __str__(self):
        return '{0}, {1}. {2}'.format(self.nombre, self.precio, self.imagen)

class Cliente(models.Model):
    nombre = models.CharField(max_length=20)
    estado = models.CharField(max_length=15, null=True)
    direccion = models.CharField(max_length=20)
    producto = models.ManyToManyField(Producto)

    def __str__(self):
        return '{0}, {1}, {2}'.format(self.nombre, self.estado, self.direccion)

class Pedidos(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.SET_NULL, null=True)
    ordenados = models.BooleanField(default=False)
    producto = models.ManyToManyField(Producto)
    fechaPedido = models.DateTimeField(auto_now=True)
    
    def get_productos(self):
        return self.producto.all()
    def __str__(self):
        return '{0} - {1}'.format(self.producto)
