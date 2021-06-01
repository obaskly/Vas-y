#!/usr/bin/python
# -*- coding: utf-8 -*-
def encrypt():


    imo = str(input("Your message: "))
    sen = imo.lower()
   
 
    encryptedString = ''
    clearString = sen
    for message in sen:
    
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
            message = '-'
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

    output = open("result", 'a')
    output.write('========')
    output.write('\n')
    output.write("Text : " + str(imo) + '\n')
    output.write("Cypher : " + str(encryptedString) + '\n')
    output.write('========\n\n')
    output.close()

    print("Clear String : ", clearString)
    print("Encrypted String : ", encryptedString)


encrypt()
