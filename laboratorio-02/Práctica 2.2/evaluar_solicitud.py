edad = int(input("Edad: "))
inscrito = input("¿Está inscrito? (si/no): ").strip().lower()
documentos = int(input("Documentos entregados: "))

cumple = edad >= 16 and inscrito == "si" and documentos >= 3

if cumple:
    print("La solicitud cumple todos los requisitos.")
else:
    print("La solicitud NO cumple. Faltan:")
    if edad < 16:
        print("- Edad mínima de 16 años")
    if inscrito != "si":
        print("- Estar inscrito")
    if documentos < 3:
        print("- Entregar al menos 3 documentos")
