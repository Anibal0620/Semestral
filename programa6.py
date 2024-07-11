def rest_numbers():
    
    print("=" * 50)
    print("	Clasificar la categoría de edad:")
    print("=" * 50)

    edad = int(input("Introduce tu edad: "))
         
    if edad >= 0 and edad <= 12:
        print("Infantil")
            
    elif edad >= 13 and edad <= 19:
        print("Adolescente")

    elif edad >= 20 and edad <= 59:
        print("Adulto")

    elif edad >= 60:
        print("Adulto mayor")

    else:
        print("Edad no válida")
