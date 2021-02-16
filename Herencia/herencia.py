class Persona:
          def __init__(self, nombre, edad, apellido, sexo):
                    self.nombre= nombre
                    self.edad = edad
                    self.apellido = apellido
                    self.sexo = sexo
          def datosPersonales(self):
                    print("Nombre: ", self.nombre)
                    print("Edad: ", self.edad)
                    print("Apellido: ", self.apellido)
                    print("Sexo: ", self.sexo)

miPersona = Persona("Angel", 36, "Araoz", "male")
miPersona.datosPersonales() 
print("\n")
print("***********  HERENCIA  ***************")
print("\n")



#Hereda todo de la clase padre              
class Empleado(Persona):
              def datosEmpleado(self, vacaciones, salario):
                        print("Vacaciones: ", vacaciones)
                        print("Salario: ", salario)
miPersona2 = Empleado("Vera", 2, "Kapanen", "female")
miPersona2.datosPersonales()
miPersona2.datosEmpleado(33, 40000)
print("***********************************")
miPersona3 = Empleado("Maria", 36, "Morales", "female")
miPersona3.datosPersonales()
miPersona3.datosEmpleado(39,100000)