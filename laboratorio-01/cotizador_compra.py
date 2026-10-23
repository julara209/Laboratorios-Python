# 1. Calcular el subtotal multiplicando el precio por la cantidad.
# 2. Convertir el porcentaje del descuento en decimal
# 3. Calcular el valor del descuento.
# 4. Calcular la base despues del descuento restando el descuento con el subtotal.
# 5. Convertir el porcentaje de impuesto a decimal.
# 6. Calcular el valor del impuesto multiplicando la base por el porcentaje del impuesto
# 7. Calcular el total fina sumando la base con el impuesto.

print("=========================")
print("    COTIZADOR PYTHON     ")
print("=========================")

cliente = str(input("Nombre del cliente: "))
vendedor = str(input("Ingresa nombre del vendedor: "))
codigo = (input("Ingresa el código de cotización: "))

producto = str(input("Nombre del producto: "))
precio_unitario = float(input("Precio unitario: "))
cantidad = int(input("Cantidad: "))
porcentaje_descuento = int(input("Descuento (%): "))
porcentaje_impuesto = int(input("Impuesto (%): "))
envio = float(input("Ingresa el costo de envío: "))

#Cálculo del subtotal
subtotal = precio_unitario * cantidad

#Conversion del descuesto a proporción
descuento = porcentaje_descuento / 100

#Calcular valor del descuento
valor_descuento = subtotal * descuento

#Cálculo de la base después del descuento
base = subtotal - valor_descuento

#Conversion del impuesto a proporción 
impuesto = porcentaje_impuesto / 100

#Calcular valor del impuesto
valor_impuesto = base * impuesto

#Cálcula del total final
total = base + valor_impuesto + envio

print ("")
print("=========================")
print("   RESUMEN DE COMPRA     ")
print("=========================")
print("Código de la cotización: ", codigo)
print("Cliente:", cliente)
print("Vendedor:", vendedor)
print("Producto:", producto)
print("Precio unitario: $", precio_unitario)
print("Cantidad:", cantidad)
print("Subtotal: $", subtotal)
print("Descuento: $", valor_descuento)
print("Base: $", base)
print("Impuesto: $", valor_impuesto)
print("Envío: $", envio)
print("TOTAL: $", total)

