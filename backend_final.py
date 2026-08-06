import conexion  # importamos el archivo de conexion
# ---- MATERIALES ----
def agregar_material(nombre, cantidad, unidad, precio):
    # Esta funcion agrega un material nuevo a la tabla Material
    # Recibe: nombre, cantidad, unidad y precio del material
    sql = "INSERT INTO Material (nombre_material, cantidad, unidad, precio_unitario) VALUES (%s, %s, %s, %s)"
    conexion.cursor.execute(sql, (nombre, cantidad, unidad, precio))
    conexion.conexion.commit()  # guardamos el cambio en la base de datos
    print("Material guardado.")

def ver_materiales():
    # Esta funcion regresa todos los materiales de la base de datos
    conexion.cursor.execute("SELECT * FROM Material")
    resultado = conexion.cursor.fetchall()  # fetchall trae todos los registros
    return resultado

def buscar_material(id_material):
    # Esta funcion busca un material por su id
    # Si no lo encuentra regresa None
    conexion.cursor.execute("SELECT * FROM Material WHERE id_material = %s", (id_material,))
    resultado = conexion.cursor.fetchone()  # fetchone trae solo un registro
    return resultado

def actualizar_material(id_material, nombre, cantidad, unidad, precio):
    # Esta funcion modifica los datos de un material que ya existe
    sql = "UPDATE Material SET nombre_material=%s, cantidad=%s, unidad=%s, precio_unitario=%s WHERE id_material=%s"
    conexion.cursor.execute(sql, (nombre, cantidad, unidad, precio, id_material))
    conexion.conexion.commit()
    print("Material actualizado.")

def eliminar_material(id_material):
    # Esta funcion borra un material de la base de datos
    conexion.cursor.execute("DELETE FROM Material WHERE id_material = %s", (id_material,))
    conexion.conexion.commit()
    print("Material eliminado.")


# ---- SERVICIOS ----

def agregar_servicio(nombre, proveedor, costo, estado):
    # Agrega un servicio nuevo a la tabla Servicios
    sql = "INSERT INTO Servicios (servicio, proveedor, costo_mensual, estado) VALUES (%s, %s, %s, %s)"
    conexion.cursor.execute(sql, (nombre, proveedor, costo, estado))
    conexion.conexion.commit()
    print("Servicio guardado.")

def ver_servicios():
    # Regresa todos los servicios de la base de datos
    conexion.cursor.execute("SELECT * FROM Servicios")
    resultado = conexion.cursor.fetchall()
    return resultado

def buscar_servicio(id_servicio):
    # Busca un servicio por su id
    conexion.cursor.execute("SELECT * FROM Servicios WHERE id_servicio = %s", (id_servicio,))
    resultado = conexion.cursor.fetchone()
    return resultado

def actualizar_servicio(id_servicio, nombre, proveedor, costo, estado):
    # Modifica los datos de un servicio existente
    sql = "UPDATE Servicios SET servicio=%s, proveedor=%s, costo_mensual=%s, estado=%s WHERE id_servicio=%s"
    conexion.cursor.execute(sql, (nombre, proveedor, costo, estado, id_servicio))
    conexion.conexion.commit()
    print("Servicio actualizado.")

def eliminar_servicio(id_servicio):
    # Borra un servicio de la base de datos
    conexion.cursor.execute("DELETE FROM Servicios WHERE id_servicio = %s", (id_servicio,))
    conexion.conexion.commit()
    print("Servicio eliminado.")

# ---- PACIENTES ----

def agregar_paciente(nombre, telefono, fecha_nac, historial):
    # Agrega un paciente nuevo a la tabla Pacientes
    sql = "INSERT INTO Pacientes (nombre, telefono, fecha_nac, historial) VALUES (%s, %s, %s, %s)"
    conexion.cursor.execute(sql, (nombre, telefono, fecha_nac, historial))
    conexion.conexion.commit()
    print("Paciente registrado.")

def ver_pacientes():
    # Regresa todos los pacientes de la base de datos
    conexion.cursor.execute("SELECT * FROM Pacientes")
    resultado = conexion.cursor.fetchall()
    return resultado

def buscar_paciente(id_paciente):
    # Busca un paciente por su id
    conexion.cursor.execute("SELECT * FROM Pacientes WHERE id = %s", (id_paciente,))
    resultado = conexion.cursor.fetchone()
    return resultado

def actualizar_paciente(id_paciente, nombre, telefono, fecha_nac, historial):
    # Modifica los datos de un paciente existente
    sql = "UPDATE Pacientes SET nombre=%s, telefono=%s, fecha_nac=%s, historial=%s WHERE id=%s"
    conexion.cursor.execute(sql, (nombre, telefono, fecha_nac, historial, id_paciente))
    conexion.conexion.commit()
    print("Paciente actualizado.")

def eliminar_paciente(id_paciente):
    # Borra un paciente de la base de datos
    conexion.cursor.execute("DELETE FROM Pacientes WHERE id = %s", (id_paciente,))
    conexion.conexion.commit()
    print("Paciente eliminado.")

def cerrar():
    # Cierra la conexion con MySQL al terminar el programa
    conexion.cursor.close()
    conexion.conexion.close()



    