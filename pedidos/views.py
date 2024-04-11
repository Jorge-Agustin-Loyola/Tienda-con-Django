from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from carro.carro import Carro
from django.contrib import messages
from pedidos.models import Pedido,LineaPedidos
from django.template.loader import render_to_string 
from django.utils.html import strip_tags
from django.core.mail import send_mail
# Create your views here.
@login_required(login_url="/autenticacion/logear")
def procesar_pedido(request):
    pedido=Pedido.objects.create(user=request.user)
    carro= Carro(request)
    lineas_pedido=list()
    for key, value in carro.carro.items():
        lineas_pedido.append(LineaPedidos(

            producto_id=key,
            cantidad=value["cantidad"],
            user=request.user,
            pedido=pedido,
        ))

    LineaPedidos.objects.bulk_create(lineas_pedido)

    enviar_mail(
        pedido=pedido,
        lineas_pedido=lineas_pedido,
        nombreusuario=request.user.username,
        emailusuario=request.user.email
    )
    messages.success(request,"El pedido se ha creado correctamente")
    return redirect("../tienda")

def enviar_mail(**kwargs):
    asunto="Gracias por el pedido"
    mensaje = render_to_string("email/pedido.html",{
        "pedido":kwargs.get("pedido"),
        "lineas_pedido":kwargs.get("lineas_pedido"),
        "nombreusuario":kwargs.get("nombreusuario"),
    })

    mensaje_texto=strip_tags(mensaje)
    from_email="agusloyola21@gmail.com"
    #to = kwargs.get("emailusuario")
    to = "agusloyola21@gmail.com"
    send_mail(asunto,mensaje_texto,from_email,[to],html_message=mensaje)