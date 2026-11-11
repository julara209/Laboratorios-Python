edad = int(input("Edad: "))
autorizacion = input("¿Tiene autorización? (si/no): ").strip().lower()

if edad >= 18:
    print("Puede ingresar.")
elif autorizacion == "si":
    print("Puede ingresar con autorización.")
else:
    print("No puede ingresar.")

