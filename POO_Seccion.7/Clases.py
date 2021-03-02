class Persona:

     #Constructor
     def __init__(self, nombre:str, apellido, edad):
          self.nombre = nombre
          self.apellido = apellido
          self.edad = edad
     def saludo(self, nombre):
          return f"Te voy saludando {self.nombre}"
class Hija(Persona):

     #Constructor
     def __init__(self, nombre, apellido, edad):
          super().__init__(nombre, apellido, edad)

# persona1 = Persona("Angel", "Araoz", 36)
# print(persona1.nombre)
# print(persona1.apellido)
# print(persona1.edad)

persona1 = Hija("Angel", "Araoz", 36)
print("Saludos para: ", )