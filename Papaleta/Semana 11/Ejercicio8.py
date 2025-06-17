def calcular_importe(compra):
    if compra > 500:
        descuento = compra * 0.12
    elif compra > 300:
        descuento = compra * 0.10
    elif compra > 300:
        descuento = compra * 0.05
    else:
        descuento = 0
    total = compra - descuento
    return total

importe = float(input("Ingrese el importe de la compra: "))
total_a_pagar = calcular_importe(importe)
print(f"El total a pagar es: ${total_a_pagar:.2f}")
