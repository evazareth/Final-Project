def pedir_numero(mensaje):
    # Le pide un numero al usuario
    # Si escribe letras en vez de numeros vuelve a preguntar (recursividad)
    try:
        numero = int(input(mensaje))
        return numero
    except ValueError:
        print("Error: escribe solo numeros.")
        return pedir_numero(mensaje)  # se llama a si misma hasta que el usuario escriba bien

def pedir_decimal(mensaje):
    # Le pide un numero con decimales al usuario
    # Tambien usa recursividad si el usuario se equivoca
    try:
        numero = float(input(mensaje))
        return numero
    except ValueError:
        print("Error: escribe un numero valido, ejemplo: 12.50")
        return pedir_decimal(mensaje)  # recursividad

def pedir_texto(mensaje):
    # Le pide un texto al usuario y no acepta campos vacios
    while True:
        texto = input(mensaje).strip()
        if texto != "":
            return texto
        print("Este campo no puede estar vacio.")

def linea():
    # Imprime una linea para separar visualmente el contenido
    print("-" * 40)