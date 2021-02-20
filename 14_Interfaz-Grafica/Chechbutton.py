from tkinter import *
def elegir():
              elegir=""

              if flores.get() ==1:
                        elegir+="Las flores"
              if aves.get() ==1:
                        elegir+="Las aves"
              if frutas.get() ==1:
                            elegir+="Las frutas"
              imprimir.config(text=elegir)                            
                            
              if flores.get() ==1 and aves.get() ==1 and frutas.get() ==1:
                        elegir+="""
                                        Has elegido todo
                                        """



root = Tk()
root.geometry("400x300")

frame = Frame(root)
frame.pack()

flores = IntVar()
aves = IntVar()
frutas = IntVar()


foto = PhotoImage(file="flores.gif")
foto1 = PhotoImage(file="aves.gif")
foto2 = PhotoImage(file="frutas.gif")


Label(root, image=foto).pack()
Label(root, image=foto1).pack()
Label(root, image=foto2).pack()


Checkbutton(root, text="Flores", variable= flores, onvalue=1, offvalue=0, command=elegir).pack()
Checkbutton(root, text="Aves", variable=aves, onvalue=1, offvalue=0, command=elegir).pack()
Checkbutton(root, text="Frutas", variable= frutas, onvalue=1, offvalue=0, command=elegir).pack()

imprimir = Label(root)
imprimir.pack()


root.mainloop()