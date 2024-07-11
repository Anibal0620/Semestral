def rest_numbers():
    
    print("="*40)
    print("Verificar si una palabara tiene 5 letras :")
    print("="*40 )

    palabra = input("Introduce una palabra: ")

    if len(palabra) > 5:
        print("La palabra tiene más de 5 letras.")

    else:
        print("La palabra tiene 5 letras o menos.")
