import conexion
from datetime import datetime
 
# ============================================================
#  FUNCIONES DE VALIDACION
#
# ============================================================
 
def pedir_numero(mensaje):
    """Pide un numero entero. Usa recursividad si el usuario se equivoca. Solo acepta enteros (no decimales)."""
    entrada = input(mensaje).strip()
    if entrada.lstrip("-").isdigit():
        return int(entrada)
    else:
        print("Error: escribe solo numeros enteros (sin decimales).")
        return pedir_numero(mensaje)  # recursividad
 
def pedir_decimal(mensaje):
    """Pide un numero decimal. Usa recursividad si el usuario se equivoca."""
    try:
        numero = float(input(mensaje))
        return numero
    except ValueError:
        print("Error: escribe un numero valido, ejemplo: 12.50")
        return pedir_decimal(mensaje)  # recursividad
 
def pedir_texto(mensaje):
    """Pide un texto. No acepta campo vacio."""
    while True:
        texto = input(mensaje).strip()
        if texto != "":
            return texto
        print("Este campo no puede estar vacio.")
 
def pedir_texto_max(mensaje, maximo):
    """Pide un texto que no puede estar vacio y no debe exceder el maximo de caracteres."""
    while True:
        texto = input(mensaje).strip()
        if texto == "":
            print("Este campo no puede estar vacio.")
        elif len(texto) > maximo:
            print(f"Error: el texto no debe exceder {maximo} caracteres.")
        else:
            return texto
 
def linea():
    """Imprime una linea separadora."""
    print("-" * 40)
 
 
# ============================================================
#  FUNCIONES DE MATERIAL
# ============================================================
 
def agregar_material():
    """Pide los datos y guarda un material en la base de datos."""
    print("\n-- Agregar material --")
    nombre   = pedir_texto("Nombre del material: ")
    cantidad = pedir_numero("Cantidad: ")
    precio   = pedir_decimal("Precio unitario: ")
    unidad   = pedir_texto("Unidad (piezas, cajas, ml): ")
 
    sql = "INSERT INTO Material (nombre_material, cantidad, precio_unitario, unidad) VALUES (%s, %s, %s, %s)"
    conexion.cursor.execute(sql, (nombre, cantidad, precio, unidad))
    conexion.conexion.commit()
    print("Material guardado.")
 
def ver_materiales():
    """Trae todos los materiales y los muestra. Retorna la lista."""
    print("\n-- Lista de materiales --")
    conexion.cursor.execute("SELECT * FROM Material")
    lista = conexion.cursor.fetchall()  # lista en memoria con todos los registros
    linea()
    if len(lista) == 0:
        print("No hay materiales registrados.")
    else:
        for m in lista:
            # m[0]=id, m[1]=nombre, m[2]=cantidad, m[3]=precio, m[4]=unidad
            print(f"ID: {m[0]} | {m[1]} | {m[2]} {m[4]} | ${float(m[3]):.2f}")
    linea()
    return lista
 
def buscar_material():
    """Busca un material por ID y lo muestra usando diccionario."""
    print("\n-- Buscar material --")
    id_buscar = pedir_numero("ID del material: ")
    conexion.cursor.execute("SELECT * FROM Material WHERE id_material = %s", (id_buscar,))
    m = conexion.cursor.fetchone()  # fetchone trae solo un registro
    if m is None:
        print("No se encontro ese material.")
    else:
        # Diccionario para mapear el registro encontrado
        material = {
            "id"     : m[0],
            "nombre" : m[1],
            "cantidad": m[2],
            "precio" : m[3],
            "unidad" : m[4]
        }
        print(f"ID       : {material['id']}")
        print(f"Nombre   : {material['nombre']}")
        print(f"Cantidad : {material['cantidad']} {material['unidad']}")
        print(f"Precio   : ${float(material['precio']):.2f}")
 
def actualizar_material():
    """Modifica los datos de un material existente."""
    ver_materiales()
    id_act   = pedir_numero("ID del material a actualizar: ")
    nombre   = pedir_texto("Nuevo nombre: ")
    cantidad = pedir_numero("Nueva cantidad: ")
    precio   = pedir_decimal("Nuevo precio: ")
    unidad   = pedir_texto("Nueva unidad: ")
 
    sql = "UPDATE Material SET nombre_material=%s, cantidad=%s, precio_unitario=%s, unidad=%s WHERE id_material=%s"
    conexion.cursor.execute(sql, (nombre, cantidad, precio, unidad, id_act))
    conexion.conexion.commit()
    print("Material actualizado.")
 
def eliminar_material():
    """Borra un material de la base de datos."""
    ver_materiales()
    id_eli = pedir_numero("ID del material a eliminar: ")
    conexion.cursor.execute("DELETE FROM Material WHERE id_material = %s", (id_eli,))
    conexion.conexion.commit()
    print("Material eliminado.")
 
 
# ============================================================
#  FUNCIONES DE SERVICIOS
# ============================================================
 
def agregar_servicio():
    """Pide los datos y guarda un servicio en la base de datos."""
    print("\n-- Agregar servicio --")
    id_ser    = pedir_texto_max("ID del servicio (maximo 5 caracteres, ej: S001): ", 5)
    nombre    = pedir_texto("Nombre del servicio: ")
    proveedor = pedir_texto("Proveedor: ")
    costo     = pedir_decimal("Costo mensual: ")
    estado    = pedir_texto("Estado (activo/inactivo): ")
 
    sql = "INSERT INTO Servicios (id_servicio, servicio, proveedor, costo_mensual, estado) VALUES (%s, %s, %s, %s, %s)"
    conexion.cursor.execute(sql, (id_ser, nombre, proveedor, costo, estado))
    conexion.conexion.commit()
    print("Servicio guardado.")
 
def ver_servicios():
    """Trae todos los servicios y los muestra. Retorna la lista."""
    print("\n-- Lista de servicios --")
    conexion.cursor.execute("SELECT * FROM Servicios")
    lista = conexion.cursor.fetchall()  # lista en memoria
    linea()
    if len(lista) == 0:
        print("No hay servicios registrados.")
    else:
        for s in lista:
            # s[0]=id, s[1]=servicio, s[2]=proveedor, s[3]=costo, s[4]=estado
            print(f"ID: {s[0]} | {s[1]} | {s[2]} | ${float(s[3]):.2f} | {s[4]}")
    linea()
    return lista
 
def buscar_servicio():
    """Busca un servicio por ID y lo muestra usando diccionario."""
    print("\n-- Buscar servicio --")
    id_buscar = pedir_texto("ID del servicio: ")
    conexion.cursor.execute("SELECT * FROM Servicios WHERE id_servicio = %s", (id_buscar,))
    s = conexion.cursor.fetchone()
    if s is None:
        print("No se encontro ese servicio.")
    else:
        # Diccionario para mapear el registro encontrado
        servicio = {
            "id"       : s[0],
            "nombre"   : s[1],
            "proveedor": s[2],
            "costo"    : s[3],
            "estado"   : s[4]
        }
        print(f"ID        : {servicio['id']}")
        print(f"Servicio  : {servicio['nombre']}")
        print(f"Proveedor : {servicio['proveedor']}")
        print(f"Costo     : ${float(servicio['costo']):.2f}")
        print(f"Estado    : {servicio['estado']}")
 
def actualizar_servicio():
    """Modifica los datos de un servicio existente."""
    ver_servicios()
    id_act    = pedir_texto("ID del servicio a actualizar: ")
    nombre    = pedir_texto("Nuevo nombre: ")
    proveedor = pedir_texto("Nuevo proveedor: ")
    costo     = pedir_decimal("Nuevo costo: ")
    estado    = pedir_texto("Nuevo estado (activo/inactivo): ")
 
    sql = "UPDATE Servicios SET servicio=%s, proveedor=%s, costo_mensual=%s, estado=%s WHERE id_servicio=%s"
    conexion.cursor.execute(sql, (nombre, proveedor, costo, estado, id_act))
    conexion.conexion.commit()
    print("Servicio actualizado.")
 
def eliminar_servicio():
    """Borra un servicio de la base de datos."""
    ver_servicios()
    id_eli = pedir_texto("ID del servicio a eliminar: ")
    conexion.cursor.execute("DELETE FROM Servicios WHERE id_servicio = %s", (id_eli,))
    conexion.conexion.commit()
    print("Servicio eliminado.")
 
 
# ============================================================
#  FUNCIONES DE PACIENTES
# ============================================================
 
def agregar_paciente():
    """Pide los datos y registra un paciente en la base de datos."""
    print("\n-- Registrar paciente --")
    nombre    = pedir_texto("Nombre completo: ")
    telefono  = pedir_texto("Telefono: ")
    fecha_nac = pedir_texto("Fecha de nacimiento (YYYY-MM-DD): ")
    historial = pedir_texto("Historial medico: ")
 
    sql = "INSERT INTO Pacientes (nombre, telefono, fecha_nac, historial) VALUES (%s, %s, %s, %s)"
    conexion.cursor.execute(sql, (nombre, telefono, fecha_nac, historial))
    conexion.conexion.commit()
    print("Paciente registrado.")
 
def ver_pacientes():
    """Trae todos los pacientes y los muestra. Retorna la lista."""
    print("\n-- Lista de pacientes --")
    conexion.cursor.execute("SELECT * FROM Pacientes")
    lista = conexion.cursor.fetchall()  # lista en memoria
    linea()
    if len(lista) == 0:
        print("No hay pacientes registrados.")
    else:
        for p in lista:
            print(f"ID: {p[0]} | {p[1]} | Tel: {p[2]} | Nac: {p[3]}")
            print(f"   Historial: {p[4]}")
    linea()
    return lista
 
def buscar_paciente():
    """Busca un paciente por ID y lo muestra usando diccionario."""
    print("\n-- Buscar paciente --")
    id_buscar = pedir_numero("ID del paciente: ")
    conexion.cursor.execute("SELECT * FROM Pacientes WHERE id = %s", (id_buscar,))
    p = conexion.cursor.fetchone()
    if p is None:
        print("No se encontro ese paciente.")
    else:
        # Diccionario para mapear el registro encontrado
        paciente = {
            "id"       : p[0],
            "nombre"   : p[1],
            "telefono" : p[2],
            "fecha_nac": p[3],
            "historial": p[4]
        }
        print(f"ID        : {paciente['id']}")
        print(f"Nombre    : {paciente['nombre']}")
        print(f"Telefono  : {paciente['telefono']}")
        print(f"Nacimiento: {paciente['fecha_nac']}")
        print(f"Historial : {paciente['historial']}")
 
def actualizar_paciente():
    """Modifica los datos de un paciente existente."""
    ver_pacientes()
    id_act    = pedir_numero("ID del paciente a actualizar: ")
    nombre    = pedir_texto("Nuevo nombre: ")
    telefono  = pedir_texto("Nuevo telefono: ")
    fecha_nac = pedir_texto("Nueva fecha de nacimiento (YYYY-MM-DD): ")
    historial = pedir_texto("Nuevo historial: ")
 
    sql = "UPDATE Pacientes SET nombre=%s, telefono=%s, fecha_nac=%s, historial=%s WHERE id=%s"
    conexion.cursor.execute(sql, (nombre, telefono, fecha_nac, historial, id_act))
    conexion.conexion.commit()
    print("Paciente actualizado.")
 
def eliminar_paciente():
    """Borra un paciente de la base de datos."""
    ver_pacientes()
    id_eli = pedir_numero("ID del paciente a eliminar: ")
    conexion.cursor.execute("DELETE FROM Pacientes WHERE id = %s", (id_eli,))
    conexion.conexion.commit()
    print("Paciente eliminado.")
 
 
# ============================================================
#  LOGICA Y REPORTES
# ============================================================
 
def verificar_stock():
    """Verifica si hay suficiente cantidad de un material."""
    id_mat   = pedir_numero("ID del material: ")
    cantidad = pedir_numero("Cantidad necesaria: ")
    conexion.cursor.execute("SELECT * FROM Material WHERE id_material = %s", (id_mat,))
    m = conexion.cursor.fetchone()
    if m is None:
        print("Material no encontrado.")
        return False
    # m[2]=cantidad, m[4]=unidad
    if m[2] >= cantidad:
        print(f"Hay suficiente stock. Disponible: {m[2]} {m[4]}")
        return True
    else:
        print(f"Stock insuficiente. Disponible: {m[2]} {m[4]}")
        return False
 
def estadisticas():
    """Muestra un resumen estadistico del sistema."""
    print("\n== ESTADISTICAS DEL SISTEMA ==")
 
    # Total de pacientes
    conexion.cursor.execute("SELECT * FROM Pacientes")
    pacientes = conexion.cursor.fetchall()  # lista en memoria
    print(f"Total de pacientes: {len(pacientes)}")
 
    # Servicios activos y costo total
    conexion.cursor.execute("SELECT * FROM Servicios")
    servicios = conexion.cursor.fetchall()  # lista en memoria
    total   = 0.0
    activos = 0
    for s in servicios:
        if s[4].lower() == "activo":
            total   = total + float(s[3])
            activos = activos + 1
    print(f"Servicios activos: {activos}")
    print(f"Costo total servicios activos: ${total:.2f}")
 
    # Materiales con poco stock (menos de 5)
    conexion.cursor.execute("SELECT * FROM Material")
    materiales = conexion.cursor.fetchall()  # lista en memoria
    criticos = []
    for m in materiales:
        if m[2] < 5:
            # Diccionario para mapear el material critico
            criticos.append({"nombre": m[1], "cantidad": m[2], "unidad": m[4]})
    print(f"Materiales con poco stock: {len(criticos)}")
    for c in criticos:
        print(f"  - {c['nombre']}: {c['cantidad']} {c['unidad']}")
 
def exportar_reporte():
    """Genera un archivo .txt con reporte de materiales y pacientes."""
    fecha          = datetime.now().strftime("%Y-%m-%d_%H-%M")
    nombre_archivo = "reporte_" + fecha + ".txt"
    archivo        = open(nombre_archivo, "w", encoding="utf-8")
 
    archivo.write("REPORTE - Clinica Dental\n")
    archivo.write("Generado: " + str(datetime.now()) + "\n")
    archivo.write("=" * 40 + "\n\n")
 
    # Seccion materiales
    archivo.write("MATERIALES:\n")
    conexion.cursor.execute("SELECT * FROM Material")
    materiales = conexion.cursor.fetchall()  # lista en memoria
    for m in materiales:
        # Diccionario para mapear cada material
        material = {"id": m[0], "nombre": m[1], "cantidad": m[2], "precio": m[3], "unidad": m[4]}
        archivo.write(f"ID: {material['id']} | {material['nombre']} | {material['cantidad']} {material['unidad']} | ${float(material['precio']):.2f}\n")
 
    # Seccion pacientes
    archivo.write("\nPACIENTES:\n")
    conexion.cursor.execute("SELECT * FROM Pacientes")
    pacientes = conexion.cursor.fetchall()  # lista en memoria
    for p in pacientes:
        archivo.write(f"ID: {p[0]} | {p[1]} | Tel: {p[2]} | Nac: {p[3]}\n")
 
    archivo.write(f"\nTotal pacientes: {len(pacientes)}\n")
    archivo.close()
    return nombre_archivo
 
 
# ============================================================
#  SUBMENUS
# ============================================================
 
def menu_material():
    """Submenu de materiales. Usa recursividad para mantenerse activo."""
    print("\n== MATERIALES ==")
    print("1. Agregar material")
    print("2. Ver materiales")
    print("3. Buscar material")
    print("4. Actualizar material")
    print("5. Eliminar material")
    print("0. Volver")
 
    opcion = pedir_numero("Elige: ")
 
    if opcion == 1:
        agregar_material()
    elif opcion == 2:
        ver_materiales()
    elif opcion == 3:
        buscar_material()
    elif opcion == 4:
        actualizar_material()
    elif opcion == 5:
        eliminar_material()
    elif opcion == 0:
        return
    else:
        print("Opcion no valida.")
 
    input("\nPresiona Enter para continuar...")
    menu_material()  # recursividad
 
def menu_servicios():
    """Submenu de servicios. Usa recursividad para mantenerse activo."""
    print("\n== SERVICIOS ==")
    print("1. Agregar servicio")
    print("2. Ver servicios")
    print("3. Buscar servicio")
    print("4. Actualizar servicio")
    print("5. Eliminar servicio")
    print("0. Volver")
 
    opcion = pedir_numero("Elige: ")
 
    if opcion == 1:
        agregar_servicio()
    elif opcion == 2:
        ver_servicios()
    elif opcion == 3:
        buscar_servicio()
    elif opcion == 4:
        actualizar_servicio()
    elif opcion == 5:
        eliminar_servicio()
    elif opcion == 0:
        return
    else:
        print("Opcion no valida.")
 
    input("\nPresiona Enter para continuar...")
    menu_servicios()  # recursividad
 
def menu_pacientes():
    """Submenu de pacientes. Usa recursividad para mantenerse activo."""
    print("\n== PACIENTES ==")
    print("1. Registrar paciente")
    print("2. Ver pacientes")
    print("3. Buscar paciente")
    print("4. Actualizar paciente")
    print("5. Eliminar paciente")
    print("0. Volver")
 
    opcion = pedir_numero("Elige: ")
 
    if opcion == 1:
        agregar_paciente()
    elif opcion == 2:
        ver_pacientes()
    elif opcion == 3:
        buscar_paciente()
    elif opcion == 4:
        actualizar_paciente()
    elif opcion == 5:
        eliminar_paciente()
    elif opcion == 0:
        return
    else:
        print("Opcion no valida.")
 
    input("\nPresiona Enter para continuar...")
    menu_pacientes()  # recursividad
 
def menu_logica():
    """Submenu de logica y reportes. Usa recursividad para mantenerse activo."""
    print("\n== LOGICA Y REPORTES ==")
    print("1. Ver estadisticas")
    print("2. Verificar stock de material")
    print("3. Exportar reporte (.txt)")
    print("0. Volver")
 
    opcion = pedir_numero("Elige: ")
 
    if opcion == 1:
        estadisticas()
    elif opcion == 2:
        verificar_stock()
    elif opcion == 3:
        archivo = exportar_reporte()
        print(f"Reporte generado: {archivo}")
    elif opcion == 0:
        return
    else:
        print("Opcion no valida.")
 
    input("\nPresiona Enter para continuar...")
    menu_logica()  # recursividad
 
 
# ============================================================
#  MENU PRINCIPAL
# ============================================================
 
def menu_principal():
    """Menu principal. Mantiene el programa activo con while hasta que el usuario salga."""
    while True:
        print("\n" + "=" * 40)
        print("  CLINICA DENTAL - Sistema de Gestion")
        print("=" * 40)
        print("1. Materiales")
        print("2. Servicios")
        print("3. Pacientes")
        print("4. Logica y Reportes")
        print("0. Salir")
 
        opcion = pedir_numero("Elige una opcion: ")
 
        if opcion == 1:
            menu_material()
        elif opcion == 2:
            menu_servicios()
        elif opcion == 3:
            menu_pacientes()
        elif opcion == 4:
            menu_logica()
        elif opcion == 0:
            print("Hasta luego.")
            break  # el break termina el while
        else:
            print("Opcion no valida.")
 
 
# Arrancamos el programa
menu_principal()
 
# Cerramos la conexion al salir
conexion.cursor.close()
conexion.conexion.close()
#terminado