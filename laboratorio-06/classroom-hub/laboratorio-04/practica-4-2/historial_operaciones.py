from pathlib import Path

ARCHIVO = Path(__file__).resolve().parent / "operaciones.txt"


def registrar():
    concepto = input("Concepto: ").strip()
    if concepto == "":
        print("El concepto no puede estar vacío.")
        return
    try:
        valor = float(input("Valor: "))
    except ValueError:
        print("El valor debe ser numérico.")
        return

    with open(ARCHIVO, "a", encoding="utf-8") as archivo:
        archivo.write(f"{concepto};{valor}\n")
    print("Operación registrada.")


def mostrar():
    try:
        with open(ARCHIVO, "r", encoding="utf-8") as archivo:
            lineas = archivo.readlines()
    except FileNotFoundError:
        print("Todavía no hay historial.")
        return

    if not lineas:
        print("El historial está vacío.")
        return
    for numero, linea in enumerate(lineas, start=1):
        concepto, valor = linea.strip().split(";")
        print(numero, "-", concepto, "-", valor)


opcion = ""
while opcion != "0":
    print()
    print("1. Registrar operación")
    print("2. Mostrar historial")
    print("0. Salir")
    opcion = input("Opción: ").strip()

    if opcion == "1":
        registrar()
    elif opcion == "2":
        mostrar()
    elif opcion == "0":
        print("Programa terminado.")
    else:
        print("Opción no válida.")
