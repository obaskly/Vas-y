from tkinter import * 
from tkinter.ttk import *
from tkinter import messagebox
from encrypt import main as enc
from decrypt import main as dec

master = Tk()
master.resizable(FALSE, FALSE)
master.title("Home")
messagebox.showinfo("Notice !", ''.join('All Rights Reserved To Bropocalypse Team'))
  
master.geometry("220x150")
  
label = Label(master, 
              text ="V 1.0")
  
label.pack(pady = 10)

btn = Button(master, 
             text ="Encrypt", 
             command = enc)
btn2 = Button(master, 
             text ="Decrypt", 
             command = dec)

btn.pack(pady = 7)
btn2.pack(pady = 7)
Quit = Button(master, text="Quit", command=master.destroy)
Quit.place(x=0, y=125)

mainloop()
