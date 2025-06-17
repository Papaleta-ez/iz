#Escribir un programa que escriba la lista de caracteres ASCII dentro de un archivo de texto.
programa = open ("ascii.txt", "r")  # Abrir el archivo en modo lectura
contenido = programa.read()  # Leer todo el contenido del archivo
print(contenido)  # Imprimir el contenido del archivo
programa.close()  # Cerrar el archivo
