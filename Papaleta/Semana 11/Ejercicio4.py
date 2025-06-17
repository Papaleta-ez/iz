def calcular_pago(horas):
    if horas <= 160:
        pago = horas * 6.5
    else:
        extra = horas - 160
        pago = (160 * 6.5) + (extra * 7.5)
    return pago

horas = float(input("Ingrese el número de horas trabajadas: "))
pago = calcular_pago(horas)
print(f"El pago total es: ${pago:.2f}")
