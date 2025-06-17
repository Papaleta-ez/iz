archi1=open("datos.txt","r+")  # Abrir el archivo en modo append
contenido  = archi1.read()  # Leer todo el contenido del archivo
print  (contenido)  # Imprimir el contenido del archivo
archi1.write("Nueva linea agregada.\n") 
archi1.write("otra linea agregada.\n")
archi1.close()  # Cerrar el archivo