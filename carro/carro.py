class Carro: 
    def __init__(self, request): #Este método se llama automáticamente cuando se crea una nueva instancia (objeto) de la clase. El constructor se utiliza para inicializar los atributos de la instancia.
        self.request=request
        self.session=request.session
        
        carro=self.session.get("carro") # session es un diccionario, esta funcion devolvera un valor asociado a la clave "carro"
        if not carro:
            carro=self.session["carro"]={}
        # else:
        self.carro=carro    
    
    def agregar(self, producto):
        if(str(producto.id) not in self.carro.keys()):
            self.carro[producto.id]={  #diccionario[clave]=valor en este caso es otro dicconario "{}"
                "producto_id":producto.id,
                "nombre":producto.nombre,
                "precio":str(producto.precio),
                "cantidad":1,
                "imagen":producto.imagen.url   
            }
        else:
            for key, value in self.carro.items(): #Recorrer pares clave-valor: Utiliza el método items() para obtener una lista de tuplas que contienen los pares clave-valor, luego puedes recorrer esta lista: 
                if key==str(producto.id):
                    value["cantidad"]=value["cantidad"]+1 #como el value en el diccionario "carro" es otro diccionario cambiamos el valor de la clave cantidad en el diccionario "value" es decir value["cantidad"]=valor nuevo
                    value["precio"]=float(value["precio"])+producto.precio
                    break # para que una vez encontrado no siga recorriendo los productos
        self.guardar_carro()
    
    def guardar_carro(self):
        self.session["carro"]=self.carro
        self.session.modified = True #. En Django, self.session.modified es una bandera booleana que se establece en True cuando se realiza una modificación en el objeto de sesión. Establecerla en True le indica a Django que debe guardar el objeto de sesión al finalizar la solicitud.
    
    def eliminar(self, producto):
        producto.id = str(producto.id)
        if producto.id in self.carro:
            del self.carro[producto.id]
            self.guardar_carro()
    
    def restar_producto(self,producto):
        for key, value in self.carro.items():
            if key == str(producto.id):
                value["cantidad"] = value["cantidad"]-1
                value["precio"]=float(value["precio"])-producto.precio
                if value["cantidad"]<1:
                    self.eliminar(producto)
                break
        self.guardar_carro()

    def limpiar_carro(self):
        self.session["carro"]={}
        self.session.modified = True 

    