from django.shortcuts import render
from Blog.models import Post,Categoria
# Create your views here.

def blog(request):
    posts= Post.objects.all
    categorias= Categoria.objects.all
    return render(request,'blog/blog.html', {'posts':posts, 'categorias':categorias})

def categorias(request, categoria_id):
    categoria = Categoria.objects.get(id= categoria_id)    
    posts=Post.objects.filter(categoria = categoria)
    return render(request, 'blog/categorias.html', {'categoria':categoria, 'posts':posts})


