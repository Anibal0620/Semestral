def rest_numbers():

    print("=" * 58)
    print("	Cálculo del Salario Mensual con Horas Extra:")
    print("=" * 58)

    def calcular_salario(horas_trabajadas, salario_por_hora, horas_extra):
        salario_base = horas_trabajadas * salario_por_hora
        salario_extra = horas_extra * salario_por_hora * 2
        salario_mensual_total = salario_base + salario_extra
        return salario_mensual_total, salario_extra

    horas_trabajadas = float(input("Ingrese las horas trabajadas en el mes: "))
    salario_por_hora = float(input("Ingrese el salario por hora: "))
    horas_extra = float(input("Ingrese el número de horas extra trabajadas: "))


    salario_total, monto_extra = calcular_salario(horas_trabajadas, salario_por_hora, horas_extra)


    print("El salario total mensual es:", salario_total)
    print("El monto adicional por horas extra es:", monto_extra)

