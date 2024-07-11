def rest_numbers():
    
    print("=" * 56)
    print("	Verificar si un número es múltiplo de 5 :")
    print("=" * 56)

    numero = int(input("Introduce un número: "))

    if numero % 5 == 0:
        print("El número es múltiplo de 5.")

    else:
        print("El número no es múltiplo de 5.")
