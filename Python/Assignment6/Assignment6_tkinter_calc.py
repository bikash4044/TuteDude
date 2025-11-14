### imports
from tkinter import *

### GUI
window = Tk()
window.geometry("500x800")


### Inputs
e = Entry(window, width = 56, borderwidth = 5)
e.pack()

def click(inp):
    res = e.get()
    e.delete(0, END)
    e.insert(0, str(res)+str(inp))

def evaluate():
    res = eval(str(e.get()))
    e.delete(0, END)
    e.insert(0, str(res))

b = Button(window, text = "1",width = 12,borderwidth = 5, command = lambda:click(1))
b.place(x = 10,y = 60)
b = Button(window, text = "2",width = 12,borderwidth = 5, command = lambda:click(2))
b.place(x = 100,y = 60)
b = Button(window, text = "3",width = 12,borderwidth = 5, command = lambda:click(3))
b.place(x = 190,y = 60)
b = Button(window, text = "4",width = 12,borderwidth = 5, command = lambda:click(4))
b.place(x = 10,y = 120)
b = Button(window, text = "5",width = 12,borderwidth = 5, command = lambda:click(5))
b.place(x = 100,y = 120)
b = Button(window, text = "6",width = 12,borderwidth = 5, command = lambda:click(6))
b.place(x = 190,y = 120)
b = Button(window, text = "7",width = 12,borderwidth = 5, command = lambda:click(7))
b.place(x = 10,y = 180)
b = Button(window, text = "8",width = 12,borderwidth = 5, command = lambda:click(8))
b.place(x = 100,y = 180)
b = Button(window, text = "9",width = 12,borderwidth = 5, command = lambda:click(9))
b.place(x = 190,y = 180)
b = Button(window, text = "0",width = 12,borderwidth = 5, command = lambda:click(0))
b.place(x = 100,y = 240)

b = Button(window, text = ".",width = 12,borderwidth = 5, command = lambda:click('.'))
b.place(x = 10,y = 240)
b = Button(window, text = "=",width = 12,borderwidth = 5, command = lambda:evaluate())
b.place(x = 190,y = 240)

b = Button(window, text = "+",width = 12,borderwidth = 5, command = lambda:click('+'))
b.place(x = 280,y = 60)
b = Button(window, text = "-",width = 12,borderwidth = 5, command = lambda:click('-'))
b.place(x = 280,y = 120)
b = Button(window, text = "*",width = 12,borderwidth = 5, command = lambda:click('*'))
b.place(x = 280,y = 180)
b = Button(window, text = "/",width = 12,borderwidth = 5, command = lambda:click('/'))
b.place(x = 280,y = 240)

b = Button(window, text = "clear",width = 12,borderwidth = 5, command= lambda:e.delete(0,END))
b.place(x = 370,y = 60)
b = Button(window, text = "<--",width = 12,borderwidth = 5, command= lambda:e.delete(END))
b.place(x = 370,y = 120)
b = Button(window, text = "(",width = 12,borderwidth = 5, command = lambda:click('('))
b.place(x = 370,y = 180)
b = Button(window, text = ")",width = 12,borderwidth = 5, command = lambda:click(')'))
b.place(x = 370,y = 240)


### mainloop
window.mainloop()