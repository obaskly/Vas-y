#!/usr/bin/python
# -*- coding: utf-8 -*-
def encrypt():


    imo = str(input("Your message: "))
    sen = imo.lower()
   
 
    encryptedString = ''
    clearString = sen
    for message in sen:
    
        if message == 'a':
            message = '/*'
        elif message == 'b':
            message = '048'
        elif message == 'c':
            message = '&'
        elif message == 'd':
            message = 'z'
        elif message == 'e':
            message = "à"
        elif message == 'f':
            message = '@'
        elif message == 'g':
            message = ')'
        elif message == 'h':
            message = '8-'
        elif message == 'i':
            message = '<'
        elif message == 'j':
            message = '>'
        elif message == 'k':
            message = '$'
        elif message == 'l':
            message = 'é'
        elif message == 'm':
            message = 'r'
        elif message == 'n':
            message = '_'
        elif message == 'o':
            message = '-'
        elif message == 'p':
            message = 'è'
        elif message == 'q':
            message = '*'
        elif message == 'r':
            message = '*/'
        elif message == 's':
            message = '+4'
        elif message == 't':
            message = '0.'
        elif message == 'u':
            message = '4-p'
        elif message == 'v':
            message = 'ç'
        elif message == 'w':
            message = '*-+'
        elif message == 'x':
            message = '+-'
        elif message == 'y':
            message = '-+'
        elif message == 'z':
            message = '0.0'
        elif message == 'é':
            message = '+6-.'
        elif message == 'è':
            message = '@ù'
        elif message == 'à':
            message = '.*.+'
        elif message == 'ç':
            message = '^14-+.^'
        elif message == '0':
            message = 'x0x'
        elif message == '1':
            message = './'
        elif message == '2':
            message = '+à'
        elif message == '3':
            message = '--++'
        elif message == '4':
            message = '+(-'
        elif message == '5':
            message = '3.20'
        elif message == '6':
            message = '<5-'
        elif message == '7':
            message = '+2./'
        elif message == '8':
            message = '-à.-'
        elif message == '9':
            message = '++9.0'
        elif message == ' ':
            message = '+.+'
        elif message == ',':
            message = '-.-'
        elif message == '.':
            message = '*-*'
        elif message == '(':
            message = '-*-'
        elif message == ')':
            message = '_-_'
        elif message == ':':
            message = '-_-'
        elif message == ';':
            message = ':)'
        elif message == '!':
            message = ':('
        elif message == '?':
            message = ':D'
        elif message == '-':
            message = ':*'
        elif message == '_':
            message = ':p'
        
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