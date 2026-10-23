def precio_valido(precio):
    return precio > 0


def cantidad_valida(cantidad):
    return cantidad > 0


def porcentaje_valido(porcentaje):
    return 0 <= porcentaje <= 100
