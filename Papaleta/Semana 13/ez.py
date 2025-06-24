import os
import getpass 
# Definimos la constante para el archivo de estudiantes
ARCHIVO = "estudiante.txt"

# Cargar usuarios desde un archivo
def cargar_usuarios():
    usuarios = {}
    if os.path.exists("usuarios.txt"):
        with open("usuarios.txt", "r") as archivo:
            for linea in archivo:
                usuario, clave = linea.strip().split(",")
                usuarios[usuario] = clave
    return usuarios

# Contraseña de acceso
clave = "Papaleta2907"

# Función para iniciar sesión
def inicio():
    print("INICIO DE SESIÓN")
    intentos = 3
    while intentos > 0:
        Intento = getpass.getpass("Ingrese la contraseña: ")
        if Intento == clave:
            print("Acceso permitido.\n")
            return True
        else:
            intentos -= 1
            print(f"Contraseña incorrecta. Intentos restantes: {intentos}")
    
    print("Acceso bloqueado. Demasiados intentos fallidos.")
    return False

# Cargar estudiantes desde un archivo
def cargar_estudiantes():
    estudiantes = []
    if os.path.exists(ARCHIVO):
        with open(ARCHIVO, "r") as archivo:
            for linea in archivo:
                codigo, nombre, apellido, carrera = linea.strip().split(",")
                estudiantes.append({
                    "codigo": codigo,
                    "nombre": nombre,
                    "apellido": apellido,
                    "carrera": carrera
                })
    return estudiantes

# Guardar estudiantes en un archivo
def guardar_estudiantes(estudiantes):
    with open(ARCHIVO, "w") as archivo:
        for est in estudiantes:
            linea = f"{est['codigo']},{est['nombre']},{est['apellido']},{est['carrera']}\n"
            archivo.write(linea)

# Crear un nuevo estudiante
def crear_estudiante(estudiantes):
    codigo = input("Código del estudiante: ")
    if any(est["codigo"] == codigo for est in estudiantes):
        print("El código ya existe\n")
        return

    nombre = input("Nombre: ")
    apellido = input("Apellido: ")
    carrera = input("Carrera: ")

    estudiantes.append({
        "codigo": codigo,
        "nombre": nombre,
        "apellido": apellido,
        "carrera": carrera
    })

    guardar_estudiantes(estudiantes)
    print("Estudiante agregado correctamente.\n")

# Mostrar la lista de estudiantes
def mostrar_estudiantes(estudiantes):
    if not estudiantes:
        print("No hay estudiantes registrados.\n")
        return

    print("\nLista de estudiantes:")
    for est in estudiantes:
        print(f"Código: {est['codigo']}, Nombre: {est['nombre']} {est['apellido']}, Carrera: {est['carrera']}")
    print()

# Actualizar la información de un estudiante
def actualizar_estudiante(estudiantes):
    codigo = input("Ingresa el código del estudiante a actualizar: ")
    for est in estudiantes:
        if est["codigo"] == codigo:
            est["nombre"] = input(f"Nuevo nombre (actual: {est['nombre']}): ") or est["nombre"]
            est["apellido"] = input(f"Nuevo apellido (actual: {est['apellido']}): ") or est["apellido"]
            est["carrera"] = input(f"Nueva carrera (actual: {est['carrera']}): ") or est["carrera"]
            guardar_estudiantes(estudiantes)
            print("Estudiante actualizado.\n")
            return
    print("No se encontró estudiante con ese código.\n")

# Eliminar un estudiante
def eliminar_estudiante(estudiantes):
    codigo = input("Ingresa el código del estudiante a eliminar: ")
    for est in estudiantes:
        if est["codigo"] == codigo:
            estudiantes.remove(est)
            guardar_estudiantes(estudiantes)
            print("Estudiante eliminado.\n")
            return
    print("No se encontró un estudiante con ese código.\n")

# Menú principal
def menu():
    estudiantes = cargar_estudiantes()
    while True:
        print("=======MENU CRUD ESTUDIANTES=======")
        print("1. Agregar estudiante")
        print("2. Mostrar estudiantes")
        print("3. Actualizar estudiante")
        print("4. Eliminar estudiante")
        print("5. Salir")   
        opcion = input("Seleccione una opción (1-5): ")
        if opcion == "1":
            crear_estudiante(estudiantes)
        elif opcion == "2":
            mostrar_estudiantes(estudiantes)
        elif opcion == "3":
            actualizar_estudiante(estudiantes)
        elif opcion == "4":
            eliminar_estudiante(estudiantes)
        elif opcion == "5":
            print("Saliendo del programa...")
            break
        else:
            print("Opción no válida. Intente de nuevo.")

# Ejecución del programa
if inicio():
    menu()
