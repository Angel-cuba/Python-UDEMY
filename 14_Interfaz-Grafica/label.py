from tkinter import *

root= Tk()
imagen = PhotoImage(file="tiger.ico")

label = Label(root, image= imagen)



text_new = StringVar()
text_new.set("Programing")


root.title("Python")
root.config(width= 400, height=350)

label = Label(root, text="Hola Angel desde Python")
# label.pack()
label.place(x=100, y=60)
label.config(bg="black", fg="white")



label = Label(root, text="Welcome")
# label.pack()
label.place(x=250, y=100)
label.config(bg="green",textvariable= text_new)



root.mainloop()