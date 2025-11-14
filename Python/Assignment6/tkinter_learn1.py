import tkinter as tk
from tkinter import font
from tkinter import ttk
window = tk.Tk()
window.title("My first window")
window.minsize(width=800,height=300)

custom_font = font.Font(family="Times New Roman", size=20, weight="bold")

label = tk.Label(window,bg="Red", text="My first App", font=custom_font)
label.pack(side="top")
label.config(font=("Times New Roman", 20))
i=0
def fnx():
    global i
    i = i + 1;
    label.config(text=f"clicked {i} times")

def fnx2():
    label.config(text=user_input.get())
button = ttk.Button(window, text="Click here", command=fnx2)
button.pack()

user_input = ttk.Entry()
user_input.pack()

user_pass = ttk.Entry(show="*")
user_pass.pack()


my_frame = ttk.Frame(window)
my_frame.pack()

label2 = tk.Label(my_frame,bg="Red", text="This is a frame", font=custom_font)
label2.pack(side="top")

button2 = ttk.Button(window, text="Exit", command=window.destroy)
button2.pack()
window.mainloop()

