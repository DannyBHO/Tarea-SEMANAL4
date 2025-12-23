from modelos.habitacion import Habitacion
from modelos.reserva import Reserva
from servicios.hotel import Hotel

# Crear hotel
hotel = Hotel("Hotel Amazonía")

# Crear habitaciones
habitacion1 = Habitacion(101, "Simple", 40)
habitacion2 = Habitacion(102, "Doble", 60)

# Agregar habitaciones
hotel.agregar_habitacion(habitacion1)
hotel.agregar_habitacion(habitacion2)

# Mostrar habitaciones disponibles
hotel.mostrar_habitaciones_disponibles()

# Realizar reserva
reserva1 = Reserva("Juan Pérez", habitacion1)
reserva1.confirmar_reserva()

# Mostrar habitaciones disponibles nuevamente
hotel.mostrar_habitaciones_disponibles()
