def rest_numbers():
    
    print("="*40)
    print("Determinar si un carácter es una vocal :")
    print("="*40 )

    letra = input("Introduce una letra: ")

    if letra == "a" or letra == "A" or letra == "e" or letra == "E" or letra == "i" or letra == "I" or letra == "o" or letra == "O" or letra == "u" or letra == "U":
        print("La letra es una vocal.")
    else:
        print("La letra no es una vocal.")
