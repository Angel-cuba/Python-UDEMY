# Saber que tipo de dato que hay en cada clave
diccio = {
          "clave1" :123,
          "clave2" : True,
          "clave3": [1,2,3]
}
print(type(diccio["clave3"]))
#saber el nombre de todas las clves
print(diccio.keys())
# saber los valores
print(diccio.values())
# los items
print(diccio.items())

################
for i, c in diccio.items():
          print(i,c)
    