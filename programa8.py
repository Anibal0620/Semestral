def rest_numbers():
    
    print("=" * 40)
    print("Calcular el precio con descuento")
    print("=" * 40)

    precio = float(input("Introduce el precio del producto: "))

    if precio > 100:
        descuento = precio * 0.10
        pre_fin = precio - descuento
        print(f"El precio final después del descuento del 10% es: ${pre_fin:.2f}")
        
    else:
        print(f"No se aplica descuento. El precio final es: ${precio:.2f}")
