def rest_numbers():

    print("=" * 62)
    print("	Determinar si un número es divisible por 3 y 5")
    print("=" * 62)

    numero = int(input("Introduce un número entero: "))

    es_divisible_por_3 = (numero % 3 == 0)
    es_divisible_por_5 = (numero % 5 == 0)

    if es_divisible_por_3 and es_divisible_por_5:
        print(f"El número {numero} es divisible por 3 y 5.")
    elif es_divisible_por_3:
        print(f"El número {numero} es divisible por 3 pero no por 5.")
    elif es_divisible_por_5:
        print(f"El número {numero} es divisible por 5 pero no por 3.")
    else:
        print(f"El número {numero} no es divisible ni por 3 ni por 5.")
