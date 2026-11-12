try:
    edad = int(input("Edad: "))
except ValueError:
    print("Error de conversión: escribe un número entero (por ejemplo 20).")
else:
    if edad < 0:
        print("La edad no puede ser negativa.")
    elif edad > 120:
        print("La edad no puede ser superior a 120.")
    else:
        print("Edad aceptada:", edad)

