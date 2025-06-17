def calcular_comision(venta1, venta2, venta3):
    total_ventas = venta1 + venta2 + venta3
    comision = total_ventas * 0.10
    return comision

n = int(input("Ingrese la cantidad de vendedores: "))
for i in range(n):
    print(f"\nVendedor {i+1}:")
    sueldo_base = float(input("Ingrese el sueldo base: "))
    venta1 = float(input("Ingrese el monto de la primera venta: "))
    venta2 = float(input("Ingrese el monto de la segunda venta: "))
    venta3 = float(input("Ingrese el monto de la tercera venta: "))
    
    comision = calcular_comision(venta1, venta2, venta3)
    total = sueldo_base + comision
    
    print(f"Comisión: ${comision:.2f}")
    print(f"Total a recibir: ${total:.2f}")
