class Venta:
    def __init__(self, cliente, producto):
        self.cliente = cliente
        self.producto = producto

    def confirmar_venta(self):
        if self.producto.vender():
            print(
                f"Venta confirmada para {self.cliente} "
                f"del producto {self.producto.nombre}"
            )
        else:
            print("El producto no está disponible")
