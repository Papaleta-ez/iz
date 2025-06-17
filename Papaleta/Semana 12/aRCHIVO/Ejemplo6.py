#Solicitando datos al usuario
nombre=input("Ingrese su nombre: ")
apellido=input("Ingrese su apellido: ")
edad=input("Ingrese su edad: ")
salario= input("Ingrese su salario: ")

linea=f"{nombre},{apellido},{edad},{salario}\n"

with open("Datos.txt", "a") as archi1:
    archi1.write(linea)  # Escribir la línea en el archivo
print("Datos guardados correctamente en el archivo Datos.txt")
