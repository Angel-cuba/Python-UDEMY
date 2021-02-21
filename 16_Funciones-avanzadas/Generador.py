def generaPares(limite):
    num = 1     
    miLista = []
    while num< limite:
              miLista.append(num*2)
              num = num+1
    return miLista
i = int(input("Numero: "))    
print(generaPares(i))

################################################################
def generaPares1(limite):
    num = 1
    miLista = []
    while num< limite:
              yield num*2
              num = num+1
retornaPares1 = generaPares1(10)
print(next(retornaPares1))