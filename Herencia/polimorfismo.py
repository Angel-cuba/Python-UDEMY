class Persona():
          def __init__(self):
                    self.celula= 12345
          def mensaje(self):
                    print("Vienes desde la clase persona")

class Obrero(Persona):
          def __init__(self):
                    self.especialista=1
          def mensaje(self):
                    print("Mensaje desde la clase Obrero")

obrero_planta =Persona()
obrero_planta.mensaje()

print("************************\n")

class Gato():
          def hablar(self):
                    print("Miau")
class Perro(Gato):
          def hablar(self):
                    print("Jau jau")
def escuchamascotas(animal):
          animal.hablar()

miMascota=Perro()
miMascota.hablar()