def rest_numbers():
    
    print("=" * 49)
    print("	Determinar si un número es primo")
    print("=" * 49)

    n0 = int(input("Introduce un número: "))

    if n0 > 1:
        for i in range(2, n0):
            if (n0 % i) == 0:
                print(f"El número {n0} no es primo.")
                break
        else:
            print(f"El número {n0} es primo.")
    else:
        print(f"El número {n0} no es primo.")


