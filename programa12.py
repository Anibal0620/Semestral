def rest_numbers():
    
    print("="* 39)
    print("	Calcular el salario neto")
    print("=" * 39)

    salario_bruto = float(input("Introduce tu salario bruto: $"))

    if salario_bruto > 2000:
        salario_neto = salario_bruto * 0.80
    else:
        salario_neto = salario_bruto

    print(f"El salario neto es: ${salario_neto:.2f}")
