def rest_numbers():

    print("=" * 46)
    print("	calcula prisma cuadrado:")
    print("=" * 46)


    def calcula_prisma_rectangular(largo, ancho, altura):
        V = (largo * ancho) * altura 
        return V


    largo = float(input("ingrese la longitud del largo: "))
    ancho = float(input("Ingrese la longitud del ancho: "))
    altura = float(input("Ingrese la altura del prisma: "))

     
    resultado = calcula_prisma_rectangular(largo, ancho,altura)
    print("El volumen del prisma rectangular es :", resultado)
