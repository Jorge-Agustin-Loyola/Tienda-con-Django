from django.shortcuts import render
from .models import Producto,CategoriaProductos
# Create your views here.
def tienda(request):
    productos = Producto.objects.all
    # categoria = CategoriaProductos.objects.filter(categoria=categoria)

    return render(request,"Tienda/tienda.html", {'productos':productos})
