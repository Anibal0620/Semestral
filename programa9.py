def rest_numbers():
    
    print("=" * 50)
    print("Determinar si un carácter es una letra o un dígito")
    print("=" * 50)

    caracter = input("Ingresa un caracter: ")

    if 'A' <= caracter <= 'Z' or 'a' <= caracter <= 'z':
        print("Letra")
        
    if '0' <= caracter <= '9': 
        print("Digito")
