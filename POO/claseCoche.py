class Coche():  #Creamos el molde
          def __init__(self):  #Aplicamos las características
                    self.marca= "Audi"
                    self.color= "rojo"
                    self.__rueda= 4
                    self.enmarcha= False

          def arrancar(self, arrancamos): #Creamos un método
                    self.enmarcha=arrancamos
                    if (self.enmarcha):
                              return "El coche está en marcha"
                    else:
                                  return"El coche se encuentra apagado"

          def __str__(self): #Se cre el segundo método
                    return "Este auto es marca {}, de color {}, tiene {} ruedas".format(self.marca, self.color, self.__rueda) 

miCoche=Coche() #Instanciar la clase
print(str(miCoche)) #Mostrarla en pantalla
print(miCoche.arrancar(False), "\n") #Encender o apagar el coche [true o false]

print("***********___OTRO____***************\n")
miCoche2 = Coche()
miCoche2.rueda = 20
print(miCoche2.arrancar(True))
print(str(miCoche2))
