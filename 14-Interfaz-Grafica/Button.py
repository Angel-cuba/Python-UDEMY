from tkinter import *

def sumar():
          resultado.set(int(var1.get()) + int(var2.get()))
              
def restar():
          resultado.set(int(var1.get()) - int(var2.get()))





root= Tk()

root.title("Project")

frame = Frame(root)
frame.pack()

var1 = StringVar()
var2 = StringVar()
resultado= StringVar()

entry1 = Entry(frame)
entry1.pack()
entry1.config(bd=10, font=("Curier 20"), textvariable=var1)


entry2 = Entry(frame)
entry2.pack()
entry2.config(bd=10, font=("Curier 20"), textvariable=var2)

entry3 = Entry(frame)
entry3.pack()
entry3.config(bd=10, font=("Curier 20"), state="disable", textvariable= resultado)


boton1= Button(frame, text="Add")
boton1.pack()
boton1.config(bd=10, font=("Curier 10"), command=sumar)

boton2= Button(frame, text="Rest")
boton2.pack()
boton2.config(bd=10, font=("Curier 10"), command=restar)




root.mainloop()