def rest_numbers():

    print("=" * 62)
    print("	Verificar si una palabra tiene más de 5 letras :")
    print("=" * 62)

    palabra = input("Digite una palabra: ")

    if len(palabra) > 5:
        print("La palabra que digito tiene mas de 5 letras")
    if len(palabra) ==5:
        print("La palabra que digito tiene 5 letras")
    else:
        print("La palabra que digito tiene menos de 5 letras")

    print("Fin de Programa")
