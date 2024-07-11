def rest_numbers():

    print("=" * 62)
    print("	Verificar si un nombre es corto, mediano o largo")
    print("=" * 62)

    nombre = input("Introduce un nombre: ")

    longitud = len(nombre)

    if longitud < 5:
        categoria = "corto"
    elif longitud <= 8:
        categoria = "mediano"
    else:
        categoria = "largo"

    print(f"El nombre '{nombre}' es de longitud {longitud} y se clasifica como nombre {categoria}.")
