#install tkinter using sudo apt-get install python3-tk
from tkinter import *
from tkinter.messagebox import showerror

#creating the GUI
root = Tk()
root.title("Pythonista Calculator")
root.geometry("265x500")
root.resizable(0, 0) #forbid user from resizing the window
root.configure(background='LightCyan2') #the background of the calculator window

entry_strvar = StringVar(root)

Label(root, text="Made in Uganda", font=("Comic San Ms",15),bg=('LightCyan2')).place(x=25,y=0)
Label(root, text='Press \'x\' twice for exponentiation', font=("Georgia", 10), bg='LightCyan2').place(x=30, y=30)

eqn_entry = Entry(root, justify=RIGHT, textvariable=entry_strvar, width=22, font=12, state='disabled')
eqn_entry.place(x=10, y=70)

# Updating root
root.update()
root.mainloop()