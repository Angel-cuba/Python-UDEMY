from io import open

fichero = open("archivo2.txt", "w")

texto = "Estamos trabajando con Python, en la parte de los cursores"

fichero.write(texto)

fichero.close()

######__Posicion del cursor__#####
fichero = open("archivo2.txt", "r")
fichero.seek(0)
print("Todo el archivo, el # indica la posicón del cursor--->",fichero.read())

#####__Control del cursor__#####
fichero = open("archivo2.txt", "r")
# fichero.seek(len(fichero.read())/2)
# print("En la mitad: ----->",fichero.read())
print(fichero.readline())

fichero.close()

