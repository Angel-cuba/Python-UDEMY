def doblar(numero):
    return numero*2
numeros = [2,4,6,7,8,9,10,11,12]
i = map(doblar, numeros)
print(list(i))

#Ejemplo con Lambda
# def dobla(numero):
#               return numero*3

numeros = [2,3,4,5,7,8,8,9,10,11,12]
i = map(lambda x: x*4, numeros) 
# for item in i:
print("Desde Lambda: ",list(i))   