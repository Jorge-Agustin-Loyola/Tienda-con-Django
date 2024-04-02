from django.urls import path
from . import views

app_name = "carro"  #  Define el espacio de nombres (app_name) para las URLs de esta aplicación. Esto es útil para diferenciar las URLs entre diferentes aplicaciones en un proyecto Django.

urlpatterns = [
    path("agregar/<int:producto_id>", views.agregar_producto, name="agregar"), # El name se utiliza para referirse a esta URL de manera única en el código Python.
    path("restar/<int:producto_id>", views.restar_producto, name="restar"),
    path("eliminar/<int:producto_id>", views.eliminar_producto , name="eliminar"),
    path("limpiar/", views.limpiar_carro , name="limpiar"),

]
