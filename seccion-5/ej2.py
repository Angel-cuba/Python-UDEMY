asignatura = ["matemática", "física", "lengua", "historia"]
print(asignatura)

for i in asignatura:
          print("Estudio " + i + " en la escuela")

esto = []
nombre = input("nombre: ")
edad = input("edad: ")          
address = input("address: ")          
telef = input("telef: ")          

persona = {"nombre": nombre, "edad": edad, "address": address, "telef": telef}
print(persona["nombre"], "tiene ", persona["edad"], "de edad", ", el mismo vive en ", persona["address"], "y su # es: ", persona["telef"])
esto.append(persona)
print("este es mi ejemplo: ",esto)
print("**************************************************************")

lista = []

u = 1
while u <= 100:
          lista.append(u)
          u = u + 1
print("el valor es: ",lista )