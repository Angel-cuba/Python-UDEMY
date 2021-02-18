#Clases y Objetos
import pickle
class Gelato():
          def __init__(self, sabor, color, volumen):
                        self.sabor = sabor
                        self.color = color
                        self.volumen = volumen
          def Print(self):
                           print("Gelato es "+ self.sabor)
                           print("Gelato es "+ self.color)
                           print("Gelato es "+ self.volumen)
gelato1 = Gelato("Sweet", "Blue", "Big")
gelato2 = Gelato("Cold", "Red", "Small")
gelato3 = Gelato("Warm", "Brown", "Big")
gelato4 = Gelato("Fruit", "Pink", "Medium")

gelato1.Print()
gelato2.Print()
gelato3.Print()
gelato4.Print()

#####################
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

persona1 = Persona("Vera", 2, "femenino")
persona2 =Persona("Maria", 39, "femenino")
persona3 = Persona("Angel", 36, "masculino")


persona1.datosPersonales()
persona2.datosPersonales()
persona3.datosPersonales()

listaPersona = [persona1, persona2, persona3]

fichero = open("Personas", "wb")
pickle.dump(listaPersona, fichero)

fichero.close()

del (fichero)

