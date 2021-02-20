from tkinter import *
root = Tk()

text = Text(root)
text.pack()
text.config(width=40, height=15, padx=15, pady=15)

label = Label(root, text="Escribe aqui adentro......")
label.pack()
label.config(bg="red", font= ("Curier, 22"))



root.mainloop()