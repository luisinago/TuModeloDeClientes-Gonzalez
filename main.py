from paquete.login import llamando_a_login
from paquete.personas import Cliente, Joe, Selena, Ed, easter_egg

while True:
        menu = int(input("Escriba el número que corresponda al archivo que desea abrir: \n 1 - Login (pre-entrega 1) \n 2 - Personas (pre-entrega 2) \n 3 - Salir \n"))
        if menu == 1:
            print("BIENVENID@ AL LOGIN (Pre-entrega 1)")
            llamando_a_login()
        elif menu == 2:
            print("BIENVENID@ A PERSONAS (Pre-entrega 2)")
            while True:
                    llamando_a_personas = int(input("Escriba el número según la opción que desee: \n 1 - Mostrar lista de personas \n 2 - Easter Egg \n 3 - Relaciones \n 4 - Salir \n"))
                    if llamando_a_personas == 1:
                            elegir_persona = input("Escriba el nombre de quien desee leer sus datos: 'Joe' 'Selena' o 'Ed' \n")
                            elegir_persona = elegir_persona.capitalize()
                            if elegir_persona == "Joe":
                                    Joe.ver_info_persona("Alwyn")
                            elif elegir_persona == "Selena":
                                    Selena.ver_info_persona("Gomez")
                            elif elegir_persona == "Ed":
                                    Ed.ver_info_persona("Sheeran")
                            else:
                                    print("Esa opción no existe. Intente nuevamente")
                            
                    elif llamando_a_personas == 2:
                            print(easter_egg)
 
                    elif llamando_a_personas == 3:
                            elegir_relacion = input("Escriba el nombre de quien desee saber la duración de su relación/amistad con Taylor: 'Joe' 'Selena' o 'Ed' \n")
                            elegir_relacion = elegir_relacion.capitalize()
                            if elegir_relacion == "Joe":
                                    Joe.relaciones("desde 2017 hasta 2023")
                            elif elegir_relacion == "Selena":
                                    Selena.relaciones("desde 2008 hasta la actualidad")
                            elif elegir_relacion == "Ed":
                                    Ed.relaciones("desde 2012 hasta la actualidad")
                            else:
                                    print("Esa opción no existe. Intente nuevamente")
                    elif llamando_a_personas == 4:
                            print("¡Hasta Luego!")
                            break
                            
                    else:
                            print("Ese número de opción no existe, inténtelo nuevamente")

        elif menu == 3:
            print("¡Hasta luego!")
            break
        elif menu != 1 or 2 or 3:
            print("Ese número de opción no existe. Intente nuevamente")