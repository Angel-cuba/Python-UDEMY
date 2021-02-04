# # #paso 1

user1 = int(input("Intrroduce el primer valor: "))
user2 =int(input("Segundo valor: "))

print("iguales", user1 ==user2)
print("diferentes", user1 != user2)
print("1 mayor que 2", user1 > user2)
print("1 menor que 2", user1 < user2)

#Paso 2
user = input("Escribe")
var1 = len(user) >= 3 and len(user)< 10
print("La lon ges mayor o igual a 3 o menor a 3", var1)

#Paso 3

numero_1 = 121212
numero_user = int(input("escribe el numero del 1 al 10: "))
numero_user *= 10
numero_1 *= numero_user
print("El numero 1 para ti es: ", numero_1)