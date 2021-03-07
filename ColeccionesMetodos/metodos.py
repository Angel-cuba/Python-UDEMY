# # Metodos 
# # .upper() y .lower()
# i = input("Ingresa nombre: ")
# print("Sun nombre es ", i.upper())

# i = input("Ingresa nombre: ")
# print("Sun nombre es ", i.lower())

# # .capitalize().....la primera letra en mayúscula
# i = input("Ingresa nombre: ")
# print("Sun nombre es ", i.capitalize())

# # Contador de un elemento
# i = "Me llamo Angel"
# print("Cantidad de veces que se encuentra la palabra ->  ", i.count("Angel"))

# find()....busca en el índice donde se encuentra la palabra
istt = "Mi nombre es y será Angel Luis "
print("Índice: ", istt.find("Angel"))
# es = istt.find("1")
# if(es):
#      print("yes sssssss")
# else:
#      print("no")

item = istt.split()

for i in item:
     if(i=="Angel"):
          print("encontrado")
     else:
          print("noooo")

# if i.find("araoz"):
#      print("--------------------Encontrado", i )
# else:
#      print("No se encuentra")

#isdigit....boolean si lo que es un tipo numérico
# i = "123"
# print("Isdigit: ", i.isdigit())

# #slpit().... separar las cadenas por espacio
# i = "Hola me llamo Angel y vivo en Finlandia"
# print(i.split())

# #isalnum----encuentra o busca los números en el string
# #no se deben dejar espacios
# i = "Finlandia123"
# print(i.isalnum())

# ##isalpha.......busca solo letras
# i = "abc"
# print(i.isalpha())

# #islower.....busca en la cadena de texto si hay letras en misnúscula
# i = "abcA"
# print(i.islower())