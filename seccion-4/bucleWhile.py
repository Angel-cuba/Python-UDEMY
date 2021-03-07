i = 0

while i <= 10:
          print("Hola mundo", i*2)
          # print("Hola mundo", i)

          i += 1
if i>10 and i<20:
    i += 3 
    print(f'3 *{i} =', i*3)                                
else:        
    print("Final del programa")   


#Otro ejemplo

edad = int(input("Ingresa una edad: "))

while edad < 10:
          print("Está mal tu edad")
          edad = int(input("Ingresa tu edad nuevamente: "))
else:
    print("Este ciclo ha finalizado")          