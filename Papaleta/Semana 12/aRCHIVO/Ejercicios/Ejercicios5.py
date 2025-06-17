#Escribir un programa que lea y muestre en pantalla el archivo generado en el ejercicio anterior.
Ejercicio5 = open("ascii.txt", "r")  # Abrir el archivo en modo lectura
contenido = Ejercicio5.read()  # Leer todo el contenido del archivo
print(contenido)  # Imprimir el contenido del archivo
Ejercicio5.close()  # Cerrar el archivo