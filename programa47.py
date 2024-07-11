def rest_numbers():
    
    print("=" * 38)
    print("	calcular impuesto:")
    print("=" * 38)


    def calcular_impuesto(precio, cantidad, tasa_impuesto):
        subtotal = precio * cantidad
        impuesto = subtotal * tasa_impuesto
        return impuesto


    precio_producto = float(input("Ingrese el precio del producto: "))


    cantidad_producto = int(input("Ingrese la cantidad de unidades: "))


    tasa_impuesto = float(input("Ingrese la tasa de impuesto (en porcentaje): ")) / 100


    impuesto_calculado = calcular_impuesto(precio_producto, cantidad_producto, tasa_impuesto)


    print("El impuesto a pagar es:", impuesto_calculado)
