def rest_numbers():


    print("=" * 49)
    print("	Determinar si un año es un siglo")
    print("=" * 49)
    year = int(input("Ingrese un año: "))

    if year % 100 == 0 and year % 400 == 0:
        print(f"{year} es el primer año de un siglo y también es un año bisiesto.")
    elif year % 100 == 0:
        print(f"{year} es el primer año de un siglo pero no es un año bisiesto.")
    else:
        print(f"{year} no es el primer año de un siglo.")
