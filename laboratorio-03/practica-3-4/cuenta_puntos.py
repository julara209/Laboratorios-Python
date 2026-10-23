class CuentaPuntos:
    def __init__(self, titular):
        self._titular = titular
        self._puntos = 0

    @property
    def titular(self):
        return self._titular

    @property
    def puntos(self):
        return self._puntos

    def sumar(self, cantidad):
        if cantidad <= 0:
            return False
        self._puntos += cantidad
        return True

    def canjear(self, cantidad):
        if cantidad <= 0 or cantidad > self._puntos:
            return False
        self._puntos -= cantidad
        return True


cuenta = CuentaPuntos("Laura")
print("Sumar 80:", "aceptado" if cuenta.sumar(80) else "rechazado")
print("Canjear 30:", "aceptado" if cuenta.canjear(30) else "rechazado")
print("Canjear 100:", "aceptado" if cuenta.canjear(100) else "rechazado")
print("Total:", cuenta.puntos)    # 50
