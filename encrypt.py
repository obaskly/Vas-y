from tkinter import Tk, Button,Entry, FALSE
from tkinter.constants import X
from tkinter.ttk import *

import base64


def main():
    global root
    root = Tk()
    root.resizable(FALSE, FALSE)
    root.title("Encryptor")
    root.geometry("220x170")
    root.configure(background='black')
 
    global e0
    e0  = Entry(root)
    b0 = Button(root, text='Encrypt', command=lambda:[passing(),bar()])
    global e1
    e1 = Entry(root)
    global progress
    progress = Progressbar(root, orient = 'horizontal',
              length = 200, mode = 'determinate')
 
 
 
    e0.pack(pady = 10)
    b0.pack(pady = 10)
 
    e1.pack(pady = 10)

    progress.pack(pady = 10)
 
    root.mainloop()

def bar():
    progress['value'] = 100
    root.update_idletasks()

def passing():
    input = e0.get()
    
    encryptedString = ''
    for message in input:
    
        if message == 'a':
            message = '؛'
        elif message == 'b':
            message = '1'
        elif message == 'c':
            message = '2'
        elif message == 'd':
            message = '3'
        elif message == 'e':
            message = "4"
        elif message == 'f':
            message = '5'
        elif message == 'g':
            message = '6'
        elif message == 'h':
            message = '7'
        elif message == 'i':
            message = '8'
        elif message == 'j':
            message = '9'
        elif message == 'k':
            message = '.'
        elif message == 'l':
            message = '+'
        elif message == 'm':
            message = '’'
        elif message == 'n':
            message = '*'
        elif message == 'o':
            message = '/'
        elif message == 'p':
            message = '='
        elif message == 'q':
            message = ')'
        elif message == 'r':
            message = "à"
        elif message == 's':
            message = 'ç'
        elif message == 't':
            message = '_'
        elif message == 'u':
            message = 'è'
        elif message == 'v':
            message = '-'
        elif message == 'w':
            message = '('
        elif message == 'x':
            message = '"'
        elif message == 'y':
            message = 'é'
        elif message == 'z':
            message = '&'
        elif message == 'é':
            message = '²'
        elif message == 'è':
            message = '}'
        elif message == 'à':
            message = ']'
        elif message == 'ç':
            message = '@'
        elif message == '0':
            message = '^'
        elif message == '1':
            message = '|'
        elif message == '2':
            message = '`'
        elif message == '3':
            message = '['
        elif message == '4':
            message = '{'
        elif message == '5':
            message = '#'
        elif message == '6':
            message = '~'
        elif message == '7':
            message = '<'
        elif message == '8':
            message = '>'
        elif message == '9':
            message = '$'
        elif message == ' ':
            message = '£'
        elif message == ',':
            message = 'µ'
        elif message == '.':
            message = 'ù'
        elif message == '(':
            message = '%'
        elif message == ')':
            message = '!'
        elif message == ':':
            message = '§'
        elif message == ';':
            message = '؟'
        elif message == '!':
            message = ','
        elif message == '?':
            message = ':'
        elif message == '-':
            message = ';'
        elif message == '_':
            message = '?'
        
        encryptedString+=message
    

    stringToEncode = encryptedString.encode("utf-8")
  
    stringIn64 = base64.b64encode(stringToEncode)    

 
    string = stringIn64.decode("utf-8")

    root.clipboard_clear()
    root.clipboard_append(str(string))
    e1.insert(0, stringIn64)
