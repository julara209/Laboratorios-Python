tareas = []
opcion = ""

while opcion != "0":
    print()
    print("1. Agregar tarea")
    print("2. Mostrar tareas")
    print("3. Consultar cantidad")
    print("0. Salir")

    opcion = input("Opción: ").strip()

    if opcion == "1":
        tarea = input("Tarea: ").strip()
        if tarea == "":
            print("La tarea no puede estar vacía.")
        else:
            tareas.append(tarea)
            print("Tarea agregada.")
    elif opcion == "2":
        if len(tareas) == 0:
            print("No hay tareas registradas.")
        else:
            for posicion, tarea in enumerate(tareas, start=1):
                print(posicion, "-", tarea)
    elif opcion == "3":
        print("Cantidad de tareas:", len(tareas))
    elif opcion == "0":
        print("Programa terminado.")
    else:
        print("Opción no válida.")
