import calculos
import validaciones


def main():
    precio = float(input("Precio: "))
    cantidad = int(input("Cantidad: "))
    descuento = float(input("Descuento (%): "))
    impuesto = float(input("Impuesto (%): "))

    if not validaciones.precio_valido(precio):
        print("El precio debe ser mayor que cero.")
    elif not validaciones.cantidad_valida(cantidad):
        print("La cantidad debe ser mayor que cero.")
    elif not validaciones.porcentaje_valido(descuento):
        print("El descuento debe estar entre 0 y 100.")
    elif not validaciones.porcentaje_valido(impuesto):
        print("El impuesto debe estar entre 0 y 100.")
    else:
        subtotal = calculos.calcular_subtotal(precio, cantidad)
        valor_descuento = calculos.calcular_descuento(subtotal, descuento)
        base = subtotal - valor_descuento
        valor_impuesto = calculos.calcular_impuesto(base, impuesto)
        total = base + valor_impuesto

        print("Subtotal:", subtotal)
        print("Descuento:", valor_descuento)
        print("Base:", base)
        print("Impuesto:", valor_impuesto)
        print("Total:", total)   


if __name__ == "__main__":
    main()
