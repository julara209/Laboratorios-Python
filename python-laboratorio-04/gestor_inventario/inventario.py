from producto import Producto


class Inventario:
    """Administra una colección propia de objetos Producto."""

    def __init__(self):
        self._productos = []

    def registrar_producto(self, producto):
        if self.buscar_por_codigo(producto.codigo) is not None:
            return False
        self._productos.append(producto)
        return True

    def listar_productos(self):
        return self._productos.copy()

    def buscar_por_codigo(self, codigo):
        for producto in self._productos:
            if producto.codigo == codigo:
                return producto
        return None

    def actualizar_existencias(self, codigo, nueva_cantidad):
        producto = self.buscar_por_codigo(codigo)
        if producto is None:
            return False
        return producto.actualizar_existencias(nueva_cantidad)

    def eliminar_producto(self, codigo):
        producto = self.buscar_por_codigo(codigo)
        if producto is None:
            return False
        self._productos.remove(producto)
        return True

    def productos_sin_stock(self):
        return [p.nombre for p in self._productos if p.cantidad == 0]

    def resumen(self):
        unidades = sum(p.cantidad for p in self._productos)
        valor = sum(p.calcular_valor() for p in self._productos)
        categorias = {p.categoria for p in self._productos}
        return {
            "productos": len(self._productos),
            "unidades": unidades,
            "valor": float(valor),
            "categorias": sorted(categorias),
        }

    def exportar_datos(self):
        """Devuelve una lista de diccionarios sin exponer la lista interna."""
        return [p.a_diccionario() for p in self._productos]

    @classmethod
    def desde_datos(cls, datos):
        """Construye un inventario NUEVO a partir de una lista de diccionarios.

        Si un registro es inválido o repetido lanza ValueError y no devuelve nada,
        de modo que nunca existe una carga parcial.
        """
        if not isinstance(datos, list):
            raise ValueError("Se esperaba una lista de productos.")
        temporal = cls()
        for numero, registro in enumerate(datos, start=1):
            try:
                producto = Producto.desde_diccionario(registro)
            except ValueError as error:
                raise ValueError(f"Registro {numero} inválido: {error}") from error
            if not temporal.registrar_producto(producto):
                raise ValueError(f"Registro {numero}: código repetido ({producto.codigo}).")
        return temporal
