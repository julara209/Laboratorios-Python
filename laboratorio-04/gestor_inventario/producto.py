import math

CATEGORIAS = ("Periféricos", "Componentes", "Accesorios")


class Producto:
    """Representa un artículo, valida sus datos y los convierte a/desde diccionarios."""

    def __init__(self, codigo, nombre, categoria, precio, cantidad):
        if not isinstance(codigo, str) or codigo.strip() == "":
            raise ValueError("El código no puede estar vacío.")
        if not isinstance(nombre, str) or nombre.strip() == "":
            raise ValueError("El nombre no puede estar vacío.")
        if categoria not in CATEGORIAS:
            raise ValueError("Categoría no permitida. Opciones: " + ", ".join(CATEGORIAS))
        if isinstance(precio, bool) or not isinstance(precio, (int, float)):
            raise ValueError("El precio debe ser un número.")
        if not math.isfinite(precio):
            raise ValueError("El precio debe ser un número finito.")
        if precio <= 0:
            raise ValueError("El precio debe ser mayor que cero.")
        if isinstance(cantidad, bool) or not isinstance(cantidad, int):
            raise ValueError("La cantidad debe ser un número entero.")
        if cantidad < 0:
            raise ValueError("La cantidad no puede ser negativa.")

        self._codigo = codigo.strip()
        self._nombre = nombre.strip()
        self._categoria = categoria
        self._precio = float(precio)
        self._cantidad = cantidad

    @property
    def codigo(self):
        return self._codigo

    @property
    def nombre(self):
        return self._nombre

    @property
    def categoria(self):
        return self._categoria

    @property
    def precio(self):
        return self._precio

    @property
    def cantidad(self):
        return self._cantidad

    def actualizar_existencias(self, nueva_cantidad):
        """Valida PRIMERO y modifica solo si el dato es aceptable."""
        if isinstance(nueva_cantidad, bool) or not isinstance(nueva_cantidad, int):
            return False
        if nueva_cantidad < 0:
            return False
        self._cantidad = nueva_cantidad
        return True

    def calcular_valor(self):
        return self._precio * self._cantidad

    def a_diccionario(self):
        return {
            "codigo": self.codigo,
            "nombre": self.nombre,
            "categoria": self.categoria,
            "precio": self.precio,
            "cantidad": self.cantidad,
        }

    @classmethod
    def desde_diccionario(cls, datos):
        """Reconstruye un Producto pasando por el constructor (con todas sus validaciones)."""
        if not isinstance(datos, dict):
            raise ValueError("Cada registro debe ser un objeto JSON (diccionario).")
        faltantes = [c for c in ("codigo", "nombre", "categoria", "precio", "cantidad") if c not in datos]
        if faltantes:
            raise ValueError("Faltan campos: " + ", ".join(faltantes))
        return cls(
            datos["codigo"],
            datos["nombre"],
            datos["categoria"],
            datos["precio"],
            datos["cantidad"],
        )
