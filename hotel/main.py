from modelos.producto import Producto
from modelos.venta import Venta
from servicios.tienda import Tienda

# Crear tienda
tienda = Tienda("hotel")

# Crear productos
producto1 = Producto("P001", "Laptop", 800)
producto2 = Producto("P002", "Mouse", 20)

# Agregar productos a la tienda
tienda.agregar_producto(producto1)
tienda.agregar_producto(producto2)

# Mostrar productos disponibles
tienda.mostrar_productos_disponibles()

# Realizar venta
venta1 = Venta("Juan Pérez", producto1)
venta1.confirmar_venta()

# Mostrar productos disponibles nuevamente
tienda.mostrar_productos_disponibles()

