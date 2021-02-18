import pickle

# lista = ["Angel","Luis","Araoz","Vera"]

# fichero = open("lista_nombre", "wb")
fichero = open("lista_nombre", "rb")


# pickle.dump(lista, fichero)
lista = pickle.load(fichero)
print(lista)

# fichero.close()