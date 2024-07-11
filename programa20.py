def rest_numbers():

    print("=" * 44)
    print("	Calcular la tarifa de un taxi")
    print("=" * 44)


    distancia = float(input("Introduce la distancia recorrida en kilómetros: "))

    ta_primeros_10_km = 2.50
    ta_adicional = 2.00

    if distancia <= 10:
        tarifa = distancia * ta_primeros_10_km
    else: 
        tarifa = 10 * ta_primeros_10_km + (distancia - 10) * ta_adicional

    print(f"La tarifa del taxi es: ${tarifa:.2f}")
