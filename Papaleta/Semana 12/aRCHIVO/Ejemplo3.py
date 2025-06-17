#Leer el contenido del arhivo de texto.txt linea a linea
archi1 = open("Datos.txt", "r")  
linea = archi1.readline()  
while linea!= '':  
    print(linea, end='')  # Imprimir la línea sin añadir un salto de línea extra
    linea = archi1.readline()  # Leer la siguiente línea
archi1.close()  