#Realice un programa que pida al usuario el nombre de un archivo de texto y, a continuación permita almacenar al usuario tantas frases como el usuario desee.
#crear un archivo de texto con el nombre proporcionado por el usuario y guardar las frases en él.
nombre_archivo = input("Ingrese el nombre del archivo de texto (con .txt al final): ")
with open(nombre_archivo, "r+") as archivo:
    while True:
        frase = input("Ingrese una frase (o 'salir' para terminar): ")
        if frase.lower() == 'salir':
            break
        archivo.write(frase + "\n")
