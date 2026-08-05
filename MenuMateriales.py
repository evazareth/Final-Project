def menu_material():
    # Muestra el submenu de materiales y llama a la funcion correcta
    # Usa recursividad para volver al menu despues de cada accion
    print("\n== MATERIALES ==")
    print("1. Agregar material")
    print("2. Ver materiales")
    print("3. Buscar material")
    print("4. Actualizar material")
    print("5. Eliminar material")
    print("0. Volver")

    opcion = pedir_numero("Elige una opcion: ")

    if opcion == 1:
        # Pedimos los datos y llamamos a la funcion del backend
        nombre   = pedir_texto("Nombre del material: ")
        cantidad = pedir_numero("Cantidad: ")
        unidad   = pedir_texto("Unidad (piezas, cajas, ml): ")
        precio   = pedir_decimal("Precio unitario: ")
        backend.agregar_material(nombre, cantidad, unidad, precio)

    elif opcion == 2:
        # Traemos todos los materiales y los mostramos con un for
        lista = backend.ver_materiales()
        linea()
        if len(lista) == 0:
            print("No hay materiales registrados.")
        else:
            for m in lista:
                # m es una tupla: m[0]=id, m[1]=nombre, m[2]=cantidad, m[3]=unidad, m[4]=precio
                print(f"ID: {m[0]} | Nombre: {m[1]} | Cantidad: {m[2]} {m[3]} | Precio: ${float(m[4]):.2f}")
        linea()

    elif opcion == 3:
        id_buscar = pedir_numero("ID del material a buscar: ")
        m = backend.buscar_material(id_buscar)
        if m is None:
            print("No se encontro ese material.")
        else:
            # Usamos un diccionario para guardar los datos del material encontrado
            material = {
                "id"      : m[0],
                "nombre"  : m[1],
                "cantidad": m[2],
                "unidad"  : m[3],
                "precio"  : m[4]
            }
            print(f"ID: {material['id']}")
            print(f"Nombre: {material['nombre']}")
            print(f"Cantidad: {material['cantidad']} {material['unidad']}")
            print(f"Precio: ${float(material['precio']):.2f}")

    elif opcion == 4:
        id_actualizar = pedir_numero("ID del material a actualizar: ")
        nombre   = pedir_texto("Nuevo nombre: ")
        cantidad = pedir_numero("Nueva cantidad: ")
        unidad   = pedir_texto("Nueva unidad: ")
        precio   = pedir_decimal("Nuevo precio: ")
        backend.actualizar_material(id_actualizar, nombre, cantidad, unidad, precio)

    elif opcion == 5:
        id_eliminar = pedir_numero("ID del material a eliminar: ")
        backend.eliminar_material(id_eliminar)

    elif opcion == 0:
        return  # regresamos al menu principal

    else:
        print("Opcion no valida.")

    input("\nPresiona Enter para continuar...")
    menu_material()  # recursividad: vuelve al menu de materiales