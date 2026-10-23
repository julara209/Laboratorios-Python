try:
    with open("pruebas.txt", "r", encoding="utf-8") as archivo:
        for numero, linea in enumerate(archivo, start=1):
            print(numero, "-", linea.strip())
except FileNotFoundError:
    print("Todavía no hay pruebas. Ejecuta bitacora.py primero.")
