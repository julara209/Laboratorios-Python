class Inventario:

    # Producto:
#   representa un artículo y controla sus valores
#
# Inventario:
#   conserva varios objetos Producto
#   registra, busca, actualiza, elimina y consulta
#
# main:
#   solicita datos
#   muestra menú
#   informa los resultados

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
