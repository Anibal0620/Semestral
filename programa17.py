def rest_numbers():   
    
    print("=" * 58)
    print("	Determinar el tipo de licencia de conducir")
    print("=" * 58)

    edad = int(input("Introduce tu edad: "))

    if edad >= 16 and edad <= 17:
        tipo_licencia = "Licencia de menor"
    elif edad >= 18 and edad <= 65:
        tipo_licencia = "Licencia de adulto"
    elif edad > 65:
        tipo_licencia = "Licencia de adulto mayor"
    else:
        tipo_licencia = "No tiene edad para obtener una licencia de conducir"


    print(f"Para una edad de {edad} años, el tipo de licencia de conducir es: {tipo_licencia}.")
