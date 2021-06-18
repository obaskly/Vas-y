from tkinter import Tk, Button,Entry, FALSE
from tkinter.constants import X
from tkinter.ttk import *

import base64


def main():
    global root
    root = Tk()
    root.resizable(FALSE, FALSE)
    root.title("Decryptor")
    root.geometry("220x170")
    root.configure(background='black')
 
    global e0
    e0  = Entry(root) 
    b0 = Button(root, text='Decrypt', command=lambda:[passing(), bar()])
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

    string = base64.b64decode(input)
    decoded = string.decode('utf-8')
    
    DecryptedString = ''

    for message in decoded:

        if message == '؛':
            message = 'a'
        elif message == '1':
            message = 'b'
        elif message == '2':
            message = 'c'
        elif message == '3':
            message = 'd'
        elif message == '4':
            message = "e"
        elif message == '5':
            message = 'f'
        elif message == '6':
            message = 'g'
        elif message == '7':
            message = 'h'
        elif message == '8':
            message = 'i'
        elif message == '9':
            message = 'j'
        elif message == '.':
            message = 'k'
        elif message == '+':
            message = 'l'
        elif message == 'D':
            message = 'm'
        elif message == '*':
            message = 'n'
        elif message == '/':
            message = 'o'
        elif message == '=':
            message = 'p'
        elif message == ')':
            message = 'q'
        elif message == 'à':
            message = "r"
        elif message == 'ç':
            message = 's'
        elif message == '_':
            message = 't'
        elif message == 'è':
            message = 'u'
        elif message == '-':
            message = 'v'
        elif message == '(':
            message = 'w'
        elif message == '"':
            message = 'x'
        elif message == 'é':
            message = 'y'
        elif message == '&':
            message = 'z'
        elif message == '²':
            message = 'é'
        elif message == '}':
            message = 'è'
        elif message == ']':
            message = 'à'
        elif message == '@':
            message = 'ç'
        elif message == '^':
            message = '0'
        elif message == '|':
            message = '1'
        elif message == '`':
            message = '2'
        elif message == '[':
            message = '3'
        elif message == '{':
            message = '4'
        elif message == '#':
            message = '5'
        elif message == '~':
            message = '6'
        elif message == '<':
            message = '7'
        elif message == '>':
            message = '8'
        elif message == '$':
            message = '9'
        elif message == '£':
            message = ' '
        elif message == 'µ':
            message = ','
        elif message == 'ù':
            message = '.'
        elif message == '%':
            message = '('
        elif message == '!':
            message = ')'
        elif message == '§':
            message = ':'
        elif message == '؟':
            message = ';'
        elif message == ',':
            message = '!'
        elif message == ':':
            message = '?'
        elif message == ';':
            message = '-'
        elif message == '?':
            message = '_'

        DecryptedString+=message
        

    x = DecryptedString
    root.clipboard_clear()
    root.clipboard_append(str(x))
    e1.insert(0, x)
