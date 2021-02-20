from tkinter import *

#variable que def el lugar de los números 
i = 0
#Aqui se declararan las funciones
def click(valor):
          global i
          entry.insert(i, valor)
          i+= 1

#Función de BORRAR 
def delete():
              entry.delete(0, END)
              i=0


#Operaciones matemáticas 
#Esta es la funcion que define las operaciones
def calculo():
              number = entry.get()
              resultado = eval(number)
              entry.delete(0, END)
              entry.insert(0, resultado)
              i=0


#Interfaz gráfica de la calculadora
root= Tk()
root.title("Calculator")
root.config(bg="gray")


#Esta es la ventana de la entrada de numeros
entry = Entry(root,font=("Curier 20"))
entry.grid(row=0, column=0, columnspan=4, padx=5, pady=5)



#Botones, a los cuales, desde aqui, se les define ciertas característica 
#*******Cada boton con su valor********
#Con __command=lambda:f(x)(#) se obtiene el valor del parámetro
button1 = Button(root, text="1",width=5, height=3, bg="lightblue", command=lambda:click(1))
button2 = Button(root, text="2",width=5, height=3, bg="lightblue", command=lambda:click(2))
button3 = Button(root, text="3",width=5, height=3, bg="lightblue", command=lambda:click(3))
button4 = Button(root, text="4",width=5, height=3, bg="lightblue", command=lambda:click(4))
button5 = Button(root, text="5",width=5, height=3, bg="lightblue", command=lambda:click(5))
button6 = Button(root, text="6",width=5, height=3, bg="lightblue", command=lambda:click(6))
button7 = Button(root, text="7",width=5, height=3, bg="lightblue", command=lambda:click(7))
button8 = Button(root, text="8",width=5, height=3, bg="lightblue", command=lambda:click(8))
button9 = Button(root, text="9",width=5, height=3, bg="lightblue", command=lambda:click(9))
button0 = Button(root, text="0",width=17, height=3, bg="lightblue", command=lambda:click(0))


button_borrar = Button(root, text="DEL",width=5, height=3, bg="crimson", command=lambda:delete())
button_parentesis1 = Button(root, text="(",width=5, height=3, bg="lightgreen", command=lambda:click("("))
button_parentesis2 = Button(root, text=")",width=5, height=3, bg="lightgreen", command=lambda:click(")"))
button_punto = Button(root, text=".",width=5, height=3, bg="silver", command=lambda:click("."))



button_div = Button(root, text="/",width=5, height=3, bg="silver", command=lambda:click("/"))
button_multi = Button(root, text="*",width=5, height=3, bg="silver", command=lambda:click("*"))
button_suma = Button(root, text="+",width=5, height=3, bg="silver", command=lambda:click("+"))
button_resta = Button(root, text="-",width=5, height=3, bg="silver", command=lambda:click("-"))
button_igual = Button(root, text="=",width=5, height=3, bg="silver", command=lambda:calculo())


#Posición de la botonera
button_borrar.grid(row=1, column=0,padx=5, pady=5)
button_parentesis1.grid(row=1, column=1,padx=5, pady=5)
button_parentesis2.grid(row=1, column=2,padx=5, pady=5)
button_div.grid(row=1, column=3,padx=5, pady=5)

button7.grid(row=2, column=0,padx=5, pady=5)
button8.grid(row=2, column=1,padx=5, pady=5)
button9.grid(row=2, column=2,padx=5, pady=5)
button_multi.grid(row=2, column=3,padx=5, pady=5)

button4.grid(row=3, column=0,padx=5, pady=5)
button5.grid(row=3, column=1,padx=5, pady=5)
button6.grid(row=3, column=2,padx=5, pady=5)
button_resta.grid(row=3, column=3,padx=5, pady=5)

button1.grid(row=4, column=0,padx=5, pady=5)
button2.grid(row=4, column=1,padx=5, pady=5)
button3.grid(row=4, column=2,padx=5, pady=5)
button_suma.grid(row=4, column=3,padx=5, pady=5)

button0.grid(row=5, column=0, columnspan=2, padx=5, pady=5)
button_punto.grid(row=5, column=2, padx=5, pady=5)
button_igual.grid(row=5, column=3, padx=5, pady=5)
# button0,button1,button2,button3.config(bg="crimson")








root.mainloop()