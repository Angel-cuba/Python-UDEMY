class Clase1:
          def saluda(self):
                    print("ClASE 1")
class Clase2:
          def saluda2(self):
                    print("Clase 2")

class Clase3(Clase1, Clase2):
          def saluda3(self):
                    print("Nuevo método de la clase número 3")

c = Clase3()
c.saluda2()
c.saluda()
c.saluda3()