BaseDatos = {}

# Registro
def REGISTRO():
    usuario = input("Escriba nombre de usuario: \n")
    contrasenia = input("Escriba contrasenia: \n")
    BaseDatos.update({usuario : contrasenia})
    return print(f"Usted se ha registrado con nombre de usuario: {usuario} y contraseña: {contrasenia}")

#Muestra de Datos
def MUESTRA():
    for key_usuario, values_contrasenia in BaseDatos.items():
        print("La información almacenada en la Base de Datos es: \n", f"Usuario: {key_usuario} \n", f"Contraseña: {values_contrasenia} \n")

#Loggearse

def LOGIN():
    try:
        while True:
            usuario = input("Ingrese con su usuario: \n")
            contrasenia = input("Ingrese con su contraseña: \n")
            if (contrasenia in BaseDatos[usuario] == contrasenia):
                print("Ha ingresado correctamente")
                break
            else:
                print("Contraseña incorrecta. Vuelva a intentarlo.")
    except:
        print("Ese usuario no existe en nuestra Base de Datos")
        LOGIN()

#Menu elegir qué hacer
def llamando_a_login():
        while True:
            try:
                Opciones = int(input("Escriba el número que corresponda según lo que desee hacer: \n 1 - Registrarse \n 2 - Mostrar Datos \n 3 - Loggearse \n 4 - Salir \n"))
                if Opciones == 1:
                    print("Usted ha elegido 1 - Registro")
                    REGISTRO()
                elif Opciones == 2:
                    print("Usted ha elegido 2 - Mostrar Datos")
                    MUESTRA()
                elif Opciones == 3:
                    print("Usted ha elegido 3 - Loggearse")
                    LOGIN()
                elif Opciones == 4:
                    print("¡Hasta Luego!")
                    break
                elif Opciones != 1 or 2 or 3 or 4:
                    print("Ese número de opción no existe. Intente nuevamente")
            except:
                print("Error. Intente ingresar un número correspondiente a una opción")
