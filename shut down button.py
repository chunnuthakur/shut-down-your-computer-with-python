from tkinter import *
import os

def shutdown():
    return os.system("shutdown /s /t 1")

def restart():
    return os.system("shutdown /s /t 1")

def logout():
     return os.system("shutdown -l")

master = Tk()
master.geometry("100x100")

master.configure(bg='light grey')

Button(master,text="shutdown",command=shutdown).place(x=20,y=20)
Button(master,text="restart",command=restart).place(x=25,y=50)
Button(master,text="log out",command=logout).place(x=20,y=80)

mainloop()