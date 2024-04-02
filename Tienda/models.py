from django.db import models

# Create your models here.

class CategoriaProductos(models.Model):
    nombre = models.CharField(max_length=50)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)

    class Meta():
        verbose_name = "categoriaProductos"
        verbose_name_plural = "categoriasProductos"

    def __str__(self):
        return self.nombre

class Producto(models.Model):
    nombre = models.CharField(max_length=50)
    categoria= models.ForeignKey(CategoriaProductos, on_delete=models.CASCADE)
    imagen = models.ImageField(upload_to="tienda", null = True, blank=True)
    precio = models.FloatField()
    disponblidad = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)
    

    class Meta():
        verbose_name = "producto"
        verbose_name_plural = "productos"

    def __str__(self):
        return self.nombre