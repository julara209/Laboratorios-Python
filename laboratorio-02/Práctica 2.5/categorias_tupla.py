categorias = ("Periféricos", "Componentes", "Accesorios", "Papelería")

for posicion, categoria in enumerate(categorias, start=1):
    print(posicion, "-", categoria)

elegida = input("Categoría: ").strip()

if elegida in categorias:
    print("Categoría válida.")
else:
    print("Categoría no registrada.")

print("Categorías disponibles:", len(categorias))
