class Coche():
          def __init__(self, marca, kilo, ano):
                    self.marca= marca
                    self.kilo= kilo
                    self.ano= ano
                    print("Se ha creado un auto", self.marca) 

          def __del__(self):
                    print("Se ha vendido el ", self.marca)

          def __str__(self):
                    return "El auto es un {}, tiene {} kilos y es del ano {}".format(self.marca, self.kilo, self.ano)

miCoche = Coche( "Audi", 2000, 1993)
print(str(miCoche))
del(miCoche)

