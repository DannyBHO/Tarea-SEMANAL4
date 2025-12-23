class Hotel:
    def __init__(self, nombre):
        self.nombre = nombre
        self.habitaciones = []

    def agregar_habitacion(self, habitacion):
        self.habitaciones.append(habitacion)

    def mostrar_habitaciones_disponibles(self):
        print("Habitaciones disponibles:")
        for h in self.habitaciones:
            if h.disponible:
                print(
                    f"Habitación {h.numero} - "
                    f"{h.tipo} - ${h.precio}"
                )
