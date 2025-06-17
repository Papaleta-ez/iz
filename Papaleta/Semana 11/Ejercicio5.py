def factorial(n):
    resultado = 1
    for i in range(1, n+1):
        resultado *= i
    return resultado

numero = int(input("Ingrese un número entero: "))
print(f"El factorial de {numero} es {factorial(numero)}")
