CATEGORIAS = ("Periféricos", "Componentes", "Accesorios")


def precio_valido(precio):
    return precio > 0


def cantidad_valida(cantidad):
    return cantidad >= 0


def nombre_valido(nombre):
    return nombre.strip() != ""


def categoria_valida(categoria, categorias):
    return categoria in categorias
