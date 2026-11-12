class Producto:
    def __init__(self, cantidad):
        self._cantidad = cantidad

    def actualizar_existencias(self, nueva_cantidad):
        if nueva_cantidad < 0:
            print("Cantidad inválida.")
            return False
        self._cantidad = nueva_cantidad
        return True


p = Producto(5)
p.actualizar_existencias(-3)
print("Cantidad conservada:", p._cantidad)    # 5
