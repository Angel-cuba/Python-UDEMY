from tkinter import *

root= Tk()

frame = Frame(root, width=500, height=400)

frame.pack()

#Esta es la parte de los inputs
entrada = Entry(frame)
entrada.grid(row=0, column=1)
entrada.config(justify="center")

entrada1 = Entry(frame)
entrada1.grid(row=1, column=1)
entrada1.config(show="*")



#Esta es la parte de los LABELS
label = Label(frame,text="Nombre: ")
label.grid(row=0, column=0, sticky="w", padx=5, pady=5)

label1 = Label(frame,text="Password")
label1.grid(row=1, column=0, padx=5, pady=5)
# label = Label(frame, text="Nombre")




root.mainloop()