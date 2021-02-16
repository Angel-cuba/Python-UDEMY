def suma(num1, num2):
    return num1+num2          

def resta(num1,num2):
              return num1-num2

def multiplicar(num1, num2):
              return num1*num2
              
def dividir(num1, num2):
          try:
              return num1/num2              
          except ZeroDivisionError:
                    print("Cant choose 0")
                    return "Invalid"
#Funciona EXCEPT pero si pongo primero un 0 y después # sigue con el programa
op1 = int(input("Introduce el primer valor: "))
op2 = int(input("Introduce el segundo valor: "))

operacion = input("Introduce la operación a realizar(suma,resta,multiplicar, dividir)")

if operacion == "suma":
          print(suma(op1,op2))

elif operacion == "resta":
    print(resta(op1,op2))

elif operacion == "multiplicar":
          print(multiplicar(op1,op2))

elif operacion == "dividir":
    print(dividir(op1,op2))

else:
    print("Upss, something went wrong")
print("Executing")    
