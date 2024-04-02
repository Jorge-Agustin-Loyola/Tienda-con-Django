from django.urls import path
from . import views



urlpatterns = [
    
    path("",views.blog, name= "blog"),
    path("categoria/<int:categoria_id>",views.categorias, name= "categoria"),
    
]

