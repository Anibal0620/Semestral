def rest_numbers():

    print("=" * 50)
    print("	Sumar números hasta un límite :")
    print("=" * 50)

    limite = 99
    suma = 0

    while suma < limite :
         numero = int(input("introducir el numero positivo: "))
         suma += numero

    print ("la suma  actual: {suma}")

    print (f"la suma a llegado a su maximo limite {suma}.")
