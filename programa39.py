def rest_numbers():

    print("=" * 56)
    print("	Determinar la categoría de un trabajador")
    print("=" * 56)

    Años=float(input("Ingrese los años de experiencia: "))

    if Años <= 2:
        print("Junior")

    if Años > 2 and Años <= 5:
        print("Semi-Senior")

    if Años > 5:
        print("Senior")
