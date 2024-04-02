from django.contrib import admin
from .models import CategoriaProductos,Producto
#Register your models here.

class CategoriaProdAdmin(admin.ModelAdmin):
    readonly_fields = ('created','updated')
class ProductoAdmin(admin.ModelAdmin):
    readonly_fields = ('created','updated')

admin.site.register(CategoriaProductos,CategoriaProdAdmin)    
admin.site.register(Producto,ProductoAdmin)