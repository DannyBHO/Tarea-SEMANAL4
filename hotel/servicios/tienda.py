class Tienda:
    def __init__(self, nombre):
        self.nombre = nombre
        self.productos = []

    def agregar_producto(self, producto):
        self.productos.append(producto)

    def mostrar_productos_disponibles(self):
        print("Productos disponibles:")
        for p in self.productos:
            if p.disponible:
                print(
                    f"Producto {p.codigo} - "
                    f"{p.nombre} - ${p.precio}"
                )
