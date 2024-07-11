def rest_numbers():

    print("=" * 80)
    print("	Cálculo de Expresiones Matemáticas con los Valores A, B y C:")
    print("=" * 80)

    a = int(input("Insertar valor de A: "))
    b = int(input("Insertar valor de B: "))
    c = int(input("Insertar valor de C: "))

    c1 = (4 * a) + (3 * b)
    c2 = (21 * a) - 18 + (8 * b) - 5
    c3 = (4 * a) + (3 * b) + 7
    c5 = (2 * a) + (3 * b) - (c ** 5)
    c6 = (2 * a) + (3 * b) - (c ** 2)

    print(c1, c2, c3, c5, c6)
