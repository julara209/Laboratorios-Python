class Almacenamiento:
    def guardar(self, datos):
        print("Guardando", len(datos), "registros")


class ServicioInventario:
    def __init__(self, almacenamiento):
        self.almacenamiento = almacenamiento       

    def guardar_inventario(self, productos):
        self.almacenamiento.guardar(productos)      


servicio = ServicioInventario(Almacenamiento())
servicio.guardar_inventario(["Teclado", "Mouse"])
