def Suma(x,y):
          return(x+y)

print(Suma(3,60))


#ejemplo hecho con Lambda
sumar = lambda a,b : a+b
print(sumar(8,9))

#Buscar # impares
impares = lambda numero : numero%2 !=0
print(impares(19))

#Revertir una cadena
revertir = lambda cadena : cadena[::-1]
print(revertir("Angel"))

#Doblar un numero
def doblar(numero):
    return numero*2
print(doblar(3))

doble = lambda numero: numero*2
print(doble(5))