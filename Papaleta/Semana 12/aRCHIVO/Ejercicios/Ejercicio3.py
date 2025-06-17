#Realice un programa que pida al usuario el nombre o ubicación de un archivo de texto y, a continuación añada texto en él hasta que el usuario lo decida.
nombre_archivo = input("Ingrese el nombre del archivo de texto (con .txt al final): ")
with open(nombre_archivo, "a") as archivo:
    while True:
        frase = input("Ingrese una frase (o 'salir' para terminar): ")
        if frase.lower() == 'salir':
            break
        archivo.write(frase + "\n")
