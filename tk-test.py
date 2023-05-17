from tkinter import *

root = Tk()
var = StringVar()
label = Label( root, textvariable=var, relief=FLAT )
label2 = Label(root, text="WHAT", relief=FLAT)

var.set("Hey!? How are you doing?")
label.pack()
label2.pack()
root.mainloop()