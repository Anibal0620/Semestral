def rest_numbers():

    print("=" * 40)
    print("	Imprimir números impares")
    print("=" * 40)

    numero = int(input("Introduce un número entero positivo: "))

    print("Números impares del 1 al", numero, ":")
    for i in range(1, numero + 1):
        if i % 2 != 0:
            print(i)
