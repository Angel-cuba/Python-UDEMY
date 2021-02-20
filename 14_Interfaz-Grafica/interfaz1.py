from tkinter import *

root= Tk()

root.title=("Angel")

root.resizable(1,1)

#Frame y sus métodos para editarlo
miFrame = Frame(root)
#dentro del pack se edita la ubicación
miFrame.pack()
miFrame.config(width= 400, height=310)
miFrame.config(cursor="boat")
miFrame.config(bg="lightblue")
miFrame.config(bd="15")
miFrame.config(relief="ridge")

root.config(cursor="pirate")
root.config(bg="green")
root.config(bd="10")
root.config(relief="ridge")

root.mainloop()