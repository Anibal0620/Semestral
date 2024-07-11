def rest_numbers():
    
    print("="*56 )
    print("	Determinar si una persona es adolescente :")
    print("="*56 )

    edad = int(input("Introduce tu edad: "))

    if edad >= 13 and edad <= 19:
        print("Eres un adolescente.")

    else:
        print("No eres un adolescente.")
