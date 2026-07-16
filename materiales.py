
import mysql.connector

conexion = mysql.connector.connect(
    host     = "localhost",
    user     = "root",
    password = "",
    database = "Clinica Dental"
)
cursor = conexion.cursor()


def agregar_material(nombre, cantidad, unidad, precio):
    sql = "INSERT INTO Material (nombre_material, cantidad, unidad, precio_unitario) VALUES (%s, %s, %s, %s)"
    cursor.execute(sql, (nombre, cantidad, unidad, precio))
    conexion.commit()


def ver_materiales():
    cursor.execute("SELECT * FROM Material")
    return cursor.fetchall()


def buscar_material(id_mat):
    cursor.execute("SELECT * FROM Material WHERE id_material = %s", (id_mat,))
    return cursor.fetchone()


def actualizar_material(id_mat, nombre, cantidad, unidad, precio):
    sql = "UPDATE Material SET nombre_material=%s, cantidad=%s, unidad=%s, precio_unitario=%s WHERE id_material=%s"
    cursor.execute(sql, (nombre, cantidad, unidad, precio, id_mat))
    conexion.commit()


def eliminar_material(id_mat):
    cursor.execute("DELETE FROM Material WHERE id_material = %s", (id_mat,))
    conexion.commit()