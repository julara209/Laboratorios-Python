class Notificacion:
    def enviar(self, mensaje):
        raise NotImplementedError("Cada tipo de notificación define su envío.")


class NotificacionCorreo(Notificacion):
    def enviar(self, mensaje):
        print(f"[CORREO] {mensaje}")


class NotificacionConsola(Notificacion):
    def enviar(self, mensaje):
        print(f"[CONSOLA] {mensaje}")


for canal in [NotificacionCorreo(), NotificacionConsola()]:
    canal.enviar("Stock bajo en Mouse")

# Beneficio: quien envía no necesita saber el tipo concreto; se pueden agregar canales
# nuevos sin tocar el código que los recorre.
# Fuera de cada notificación deben quedar: decidir CUÁNDO enviar, armar el mensaje
# y obtener los datos del inventario.
