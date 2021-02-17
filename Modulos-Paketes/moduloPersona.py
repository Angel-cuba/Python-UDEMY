class Persona():
          def __init__(self, nombre, edad, sexo):
          #       super(Persona, self).__init__(nombre, edad, sexo)  
                 self.nombre = nombre
                 self.edad = edad
                 self.sexo = sexo      
          def datosPersonales(self):
              print("Nombre: ", self.nombre)
              print("Edad", self.edad)
              print("Sexo",self.sexo)

# persona1 = Persona("Vera", 2, "femenino")
# persona2 =Persona("Maria", 39, "femenino")
# persona3 = Persona("Angel", 36, "masculino")


# persona1.datosPersonales()
# persona2.datosPersonales()
# persona3.datosPersonales()