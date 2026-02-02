from tkinter import *

root = Tk()

button = Button(root,text="Send")
button.pack(side=BOTTOM)
entry  =Entry()
entry.pack(side=BOTTOM)

listbox = Listbox(root)
listbox.pack()



root.mainloop()