diccionario = {"Angel":"Araoz", "Vera": "Kapanen", "Mariam": "Caridad"}
print(diccionario["Vera"])

diccionario["Nuevo"] = "elemento"
print(diccionario)

diccionario["Nuevo"] = "este elemento"
print(diccionario)

del(diccionario["Nuevo"])
print(diccionario)

