class Reserva:
    def __init__(self, cliente, habitacion):
        self.cliente = cliente
        self.habitacion = habitacion

    def confirmar_reserva(self):
        if self.habitacion.reservar():
            print(
                f"Reserva confirmada para {self.cliente} "
                f"en la habitación {self.habitacion.numero}"
            )
        else:
            print("La habitación no está disponible")
