from io import open

fichero = open("archivo.txt", "w")#crea y abre un archivo

texto = "Hola mundo \n Estudio Python"
fichero.write(texto) # Manipular el texto
fichero.close()

##############################
fichero = open("archivo.txt", "r")
texto = fichero.read()
fichero.close()
print(texto)

#################################
fichero = open("archivo.txt", "r")
linea = fichero.readlines()
fichero.close()
print(linea)

####################
# fichero = open("archivo.txt", "a")
# fichero.write("n aaaaaaaaaaaaaaaaa")
# fichero.close()
# print(fichero)
