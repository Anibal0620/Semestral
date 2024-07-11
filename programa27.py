def rest_numbers():

    print("="*40)
    print("	Contador de dígitos:")
    print("="*40)

    numero = int(input("Ingrese un número entero: "))
    cd = 0

    while numero != 0:
        numero //= 10
        cd += 1

    print("El número tiene", cd, "dígitos.")
