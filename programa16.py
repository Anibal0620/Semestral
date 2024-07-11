def rest_numbers():

    print("=" * 35)
    print("	Clasificar el IMC")
    print("=" * 35)


    peso = float(input("Introduce tu peso en kilogramos: "))
    altura = float(input("Introduce tu altura en metros: "))

    imc = peso / (altura ** 2)

    if imc < 18.5:
        clasificacion = "Bajo peso"
    elif imc < 25:
        clasificacion = "Normal"
    elif imc < 30:
        clasificacion = "Sobrepeso"
    else:
        clasificacion = "Obesidad"

    print(f"Tu IMC es: {imc:.2f}")
    print(f"Clasificación: {clasificacion}")
