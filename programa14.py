def rest_numbers():
    
    print("=" * 50)
    print("	Verificar si un triángulo es válido")
    print("=" * 50)

    la1 = float(input("Introduce la longitud del primer lado: "))
    la2 = float(input("Introduce la longitud del segundo lado: "))
    la3 = float(input("Introduce la longitud del tercer lado: "))

    if (la1 + lado2 > la3) and (la1 + la3 > lado2) and (la2 + la3 > la1):
        print("El triángulo es válido.")
            
    else:
        print("El triángulo no es válido.")
