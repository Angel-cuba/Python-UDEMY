from tkinter import *
from tkinter import messagebox

def out():
       i = messagebox.askquestion("Salir","Are u sure?")
       if  i == "yes":
        root.destroy()
def about():
              messagebox.showinfo("Information","All is made it for me")

def licence():
          # messagebox.showwarning("Warning place")
          messagebox.showinfo("Licence","This product is under development of MonsterDeveloper")


root= Tk()

barMenu = Menu(root)
root.config(menu=barMenu)


fileMenu = Menu(barMenu, tearoff=0)
barMenu.add_cascade(label="File", menu=fileMenu)
fileMenu.add_command(label="New file")
fileMenu.add_command(label="New window")
fileMenu.add_separator()
fileMenu.add_command(label="Close", command=out)



fileEdit = Menu(barMenu, tearoff=0)
barMenu.add_cascade(label="Edit", menu=fileEdit)
fileEdit.add_command(label="Undo")
fileEdit.add_command(label="Do it again")


fileHelp = Menu(barMenu, tearoff=0)
barMenu.add_cascade(label="Help", menu=fileHelp)
fileHelp.add_command(label="About .....", command=about)
fileHelp.add_command(label="Licence", command=licence)

root.mainloop()