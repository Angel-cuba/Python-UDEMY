def saludar(nombre, edad):
    return "Hola me llamo " + nombre + ", tengo " + edad + " anos"
print(saludar("Luis", "36"))

###########################################
def validar(email):
    find = "@"
    emailValid = False
    for item in email:
                  if item == find:
                                return True
    return False
address = input("Email: ")
if validar(address):
              print("Valid")
else:
    print("Invalid")  

#################################################
def infinito(*args):
      for args in args:
             print(args)

infinito("Hola", "AAAA", [848484])   
#####__CLAVE Y VALOR___###############
def FunctionName(**kwargs):
    print(kwargs)

FunctionName(a = "Angel", b= 30, c=["Luis", "Vera"])                 

#####################################
def generapares(limite):
    num = 1
    miLista = []
  
    while num < limite:
        miLista.append(num*2)
        num=num+1

    return miLista

print(generapares(20))    