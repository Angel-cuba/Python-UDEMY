edades = [12, 34, 33, 22, 19, 2, 14, 13,9, 2000]

def old(edad):
    return edad>=18

#Filter usado para filtrar una lista
lista_edad = list(filter(old, edades))
print(lista_edad)