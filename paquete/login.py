BaseDatos = {}

# Registro
def registro_funcion():
    usuario = input("Escriba nombre de usuario: \n")
    if (usuario not in BaseDatos):
        contrasenia = input("Escriba contraseña: \n")
        BaseDatos.update({usuario : contrasenia})
        return print(f"Usted se ha registrado con nombre de usuario: {usuario} y contraseña: {contrasenia}")
    else:
        print("Ya existe ese nombre de usuario, por favor cree otro.")
        registro_funcion()

#Muestra de Datos
def muestra_funcion():
    for key_usuario, values_contrasenia in BaseDatos.items():
        print("La información almacenada en la Base de Datos es: \n", f"Usuario: {key_usuario} \n", f"Contraseña: {values_contrasenia} \n")

#Loggearse

def login_funcion():
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
        login_funcion()

#Menu elegir qué hacer
def llamando_a_login():
        while True:
            try:
                Opciones = int(input("Escriba el número que corresponda según lo que desee hacer: \n 1 - Registrarse \n 2 - Mostrar Datos \n 3 - Loggearse \n 4 - Salir \n"))
                if Opciones == 1:
                    print("Usted ha elegido 1 - Registro")
                    registro_funcion()
                elif Opciones == 2:
                    print("Usted ha elegido 2 - Mostrar Datos")
                    muestra_funcion()
                elif Opciones == 3:
                    print("Usted ha elegido 3 - Loggearse")
                    login_funcion()
                elif Opciones == 4:
                    print("¡Hasta Luego!")
                    break
                elif Opciones != 1 or 2 or 3 or 4:
                    print("Ese número de opción no existe. Intente nuevamente")
            except:
                print("Error. Intente ingresar un número correspondiente a una opción")
