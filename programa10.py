def rest_numbers():
    
    print("=" * 30)
    print("Comparar dos números")
    print("=" * 30 )

    a = int(input("ingrese un numero: "))
    b = int(input("ingrese un segundo numero: "))

    if a == b:
        print("ambos son iguales")
        
    elif a > b:
        print(f'el numero mañor es {a}')
        print(f'el numero menor es {b}')
        
    elif a < b:
        print(f'el numero mañor es {b}')
        print(f'el numero menor es {a}')
