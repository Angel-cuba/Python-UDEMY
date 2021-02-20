from tkinter import *

def show():
              if opcions.get()==1:
                 label2.config(text="Masculino", bg="red")
              else:
                        label2.config(text="Femenino", bg="blue")


root= Tk()

opcions=IntVar()

label1 = Label(root, text="Elige género.....")
label1.pack()
label1.config(bg="green")
Radiobutton(root,text="Masculino", variable=opcions, value=1, command=show).pack()

Radiobutton(root,text="Femenino", variable=opcions, value=2, command=show).pack()


label2 = Label(root)
label2.pack()


root.mainloop()