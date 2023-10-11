class Cliente:
        def __init__ (self, nombre, edad, nacionalidad, album):
                self.nombre = nombre
                self.edad = edad
                self.nacionalidad = nacionalidad
                self.__album = album
        
        def __str__(self):
                return f"Se hace alusión a {self.nombre} en los álbums: \n{self.__album}"
        
        def ver_info_persona(self, apellido):
                self.apellido = apellido
                print(f"Nombre Completo: {self.nombre} {self.apellido} \nEdad: {self.edad} \nNacionalidad: {self.nacionalidad}")
        
        def relaciones(self, relacion):
                self.relacion = relacion
                print(f"La relación/amistad entre Taylor y {self.nombre} ha durado {self.relacion}")     

#Personas/Clientes
Joe = Cliente("Joe", 32, "Inglesa", ["Reputation", "Lover", "Folklore", "Evermore", "Midnights"])

Selena = Cliente("Selena", 31, "Estadounidense", ["1989", "Evermore"])

Ed = Cliente("Ed", 32, "Inglesa", ["RED", "Reputation"])

#__str__
Kanye = Cliente("Kanye", 46, "Estadounidense", ["Speak Now", "Reputation", "Folklore", "Evermore"])

easter_egg = Kanye