#Changing the code won't make you a coder
from tkinter import * 
from tkinter.ttk import *
from tkinter import messagebox
from encrypt import main as enc
from decrypt import main as dec

def main():
    master = Tk()
    master.resizable(FALSE, FALSE)
    master.title("Home")
    messagebox.showinfo("Notice !", ''.join('All Rights Reserved To Bropocalypse Team'))
    
    master.geometry("220x200")
    
    label = Label(master, 
                text ="V 2.0")
    
    label.pack(pady = 10)

    btn = Button(master, 
                text ="Generate Public/Private Key", 
                command = gen)

    btn2 = Button(master, 
                text ="Encrypt", 
                command = enc)
    btn3 = Button(master, 
                text ="Decrypt", 
                command = dec)

    btn4 = Button(master, 
                text ="Quit", 
                command = master.destroy)
                
    btn.pack(pady = 7)
    btn2.pack(pady = 7)
    btn3.pack(pady = 7)
    btn4.pack(pady = 7)

    master.mainloop()

def gen():
    from Crypto.PublicKey import RSA
    #generate private key
    key = RSA.generate(2048)
    private_key = key.export_key()
    file_out = open("private.pem", "wb")
    file_out.write(private_key)
    file_out.close()
    #generate public key
    public_key = key.publickey().export_key()
    file_out = open("public.pem", "wb")
    file_out.write(public_key)
    file_out.close()

main()
