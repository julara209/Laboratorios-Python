try:
    a = float(input("Dividendo: "))
    b = float(input("Divisor: "))
except ValueError:
    print("Entrada no numérica: escribe números válidos.")
else:
    try:
        resultado = a / b
    except ZeroDivisionError:
        print("No se puede dividir entre cero.")
    else:
        print("Resultado:", resultado)

