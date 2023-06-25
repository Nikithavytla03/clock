from tkinter import *
from tkinter.ttk import *
from time import strftime
root=Tk()
root.title('Clock')
def time():
    string=strftime('%H:%M:%S %p')
    label.config(text=string)
    '''used to time function for every one second i.e 1000 value'''
    label.after(1000,time) 

label=Label(root, font=("ds-digital",80), background="black",foreground="cyan")
label.pack(anchor='center')
time()
mainloop()
