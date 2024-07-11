def rest_numbers():

    print("="*36)
    print("	Repetir una cadena:")
    print("="*36)


    c = input("Ingresa una cadena de texto: ")
    N = int(input("Ingresa un número entero positivo para repetir la cadena: "))

    if N > 0:
        for i in range(N):
            print(c)
    else:
        print("El número ingresado no es positivo.")
