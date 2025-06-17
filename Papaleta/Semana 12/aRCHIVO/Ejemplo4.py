archi1=open("Datos.txt", "r")  # Modo lectura
lineas = archi1.readlines()  # Leer todas las líneas del archivo
print("El archivo tiene",len   (lineas),"lineas")
print("El contenido del archivo es:")
for linea in lineas:  # Iterar sobre cada línea
    print(linea, end='')  # Imprimir la línea sin añadir un salto de línea extra
archi1.close()  # Cerrar el archivo