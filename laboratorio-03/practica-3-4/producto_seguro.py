class Producto:
    def __init__(self, codigo, nombre, precio, cantidad):
        self._codigo = codigo
        self._nombre = nombre
        self._precio = precio
        self._cantidad = cantidad

    def calcular_valor(self):
        return self._precio * self._cantidad

    @property
    def codigo(self):
        return self._codigo

    @property
    def nombre(self):
        return self._nombre

    @property
    def cantidad(self):
        return self._cantidad

    def actualizar_existencias(self, nueva_cantidad):
        if nueva_cantidad < 0:
            return False
        self._cantidad = nueva_cantidad
        return True

    @property
    def precio(self):
        return self._precio

    @precio.setter
    def precio(self, nuevo_precio):
        if nuevo_precio <= 0:
            raise ValueError("El precio debe ser mayor que cero.")
        self._precio = nuevo_precio


producto = Producto("P001", "Teclado", 85000, 4)
print(producto.calcular_valor())      # 340000
print(producto.codigo, producto.nombre, producto.cantidad)

print(producto.actualizar_existencias(10))   
print(producto.cantidad)                     
print(producto.actualizar_existencias(-5))   
print(producto.cantidad)                     

producto.precio = 90000
print(producto.precio)                      

try:
    producto.precio = -100
except ValueError as error:
    print("Error:", error)

try:
    producto.codigo = "P999"                
except AttributeError:
    print("El código no se puede cambiar.")
