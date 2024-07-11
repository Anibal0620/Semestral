def rest_numbers():
    
    print("=" * 69 )
    print("	Verificar si un número es positivo, negativo o cero :")
    print("=" * 69 )

    nu = float(input("Introduce un número: "))
    if nu > 0:
        print("El número es positivo.")
    elif nu < 0:
        print("El número es negativo.")
    else: 
        print("El número es cero.")
