import conexion
from datetime import datetime

# ============================================================
#  FUNCIONES DE VALIDACION
#  
# ============================================================

def pedir_numero(mensaje):
    """Pide un numero entero. Usa recursividad si el usuario se equivoca."""
    try:
        numero = int(input(mensaje))
        return numero
    except ValueError:
        print("Error: escribe solo numeros.")
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

def linea():
    """Imprime una linea separadora."""
    print("-" * 40)
