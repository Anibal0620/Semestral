def rest_numbers():

    print("=" * 56)
    print("	Determinar si una persona es adolescente :")
    print("=" * 56)

    usuario = float(input("Digite su edad: "))

    if usuario <10:
       print("No es un adolescente")

    if usuario  >10:
       print("Usted es un adolescente")
       
    print("Fin del programa")
