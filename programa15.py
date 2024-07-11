def rest_numbers():

    print("=" * 54)
    print("	Determinar la categoría de un trabajador")
    print("=" * 54)

    años_exp = int(input("Introduce los años de experiencia: "))

    if años_exp < 2:
        categoria = "Junior"
    elif años_exp >= 2 and años_exp <= 5:
        categoria = "Semi-Senior"
    else:
        categoria = "Senior"

    print(f"El trabajador tiene {años_expe} años de experiencia y es de categoría {categoria}.")
