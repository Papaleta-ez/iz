#Realice un programa que pida al usuario el nombre o ubicación de un archivo de texto y, a continuación de lectura a todo el archivo
# y muestre su contenido en pantalla.
try:
    archivo = open("archivo_inexistente.txt", "r")  # Intenta abrir un archivo que no existe
    contenido = archivo.read()
    print(contenido)
    archivo.close()
except FileNotFoundError:
    print("El archivo no se encontró")
