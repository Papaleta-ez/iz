#.- Lectura de un archivo de texto simple
# Escribe un programa que lea un archivo de texto llamado “poema.txt” e imprima su contenido línea por línea.
arch1=open("Poema.txt","r") #Abriendo el archivo en modo lectura y escritura
contenido = arch1.read() # Lee el contenido del archivo
print(contenido)  # Imprime el contenido del archivo
arch1.close()  # Cierra el archivo después de leer
print("Fin del programa")
