import mysql.connector

def obtener_conexion():
    """
    Crea la conexion a la base de datos MySQL.
    
    """
    conexion = mysql.connector.connect(
        host     = "localhost",
        user     = "root",
        password = "",
        database = "Clinica Dental"
    )
    return conexion

# Conexion y cursor globales para usar en todo el proyecto
conexion = obtener_conexion()
cursor   = conexion.cursor()
