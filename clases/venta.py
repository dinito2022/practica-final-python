import datetime

class Venta: #CONSTRUCTOR
    def __init__(self, cliente,lista_de_producto):
        self.cliente =cliente
        self.lista_de_producto =lista_de_producto
        self.fecha = datetime.now()
        self.total = self.calcular_total()

    def calcular_total(self):
        return sum(producto.precio for producto in self.lista_de_producto)
    
    def registrar_venta(self):
        self.cliente.registrar_compra(self)
        return f"Venta registrada:{self.mostrar_informacion()}"
    
    def mostrar_informacion(self):
        productos = ", ".join([producto.nombre for producto in self.lista_de_producto])
        return f"Cliente: {self.cliente.nombre}, Productos: {productos}, Total: {self.total}"