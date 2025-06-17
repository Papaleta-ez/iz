#Ejemplo de lectura de un archivo de texto
archi1 = open("Datos.txt", "r")  # Modo lectura
contenido = archi1.read()  # Leer todo el contenido del archivo
print(contenido)  # Imprimir el contenido del archivo
archi1.close()  # Cerrar el archivo