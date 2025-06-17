#Ejemplifucando archivos de texto en python
#Creando el archivo datos.txt
arch1=open("Datos.txt","a")
arch1.write("Primera linea.\n")
arch1.write("Segunda linea.\n")
arch1.write("Tercera linea.\n")
arch1.write("Fin del programa.\n")
arch1.close() #Cerrando el archivo
print("Fin del programa")
