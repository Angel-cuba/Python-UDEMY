from tkinter import *
from tkinter import filedialog

root = Tk()
# root.config(width=300, height=200)

def open():
          file = filedialog.askopenfilename(title="Open", initialdir="D:")
          print(file)

Button(root,text="Files", command= open).pack()

root.mainloop()