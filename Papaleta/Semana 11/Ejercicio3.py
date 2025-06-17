def descuento_renta(salario):
    return salario * 0.10

cantidad = int(input("Ingrese la cantidad de empleados: "))

for i in range(cantidad):
    salario = float(input(f"Ingrese el salario del empleado {i+1}: "))
    descuento = descuento_renta(salario)
    total = salario - descuento
    
    print(f"Descuento de renta: ${descuento:.2f}")
    print(f"Total a pagar: ${total:.2f}\n")
