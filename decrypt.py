#!/usr/bin/python
# -*- coding: utf-8 -*-
def decrypt():
    imo = str(input("Your message: "))
    sen = imo.lower()
   
    DecryptedString = ''
    clearString = sen
    for message in sen:

        if message == '/*':
            message = 'a'
        elif message == '048':
            message = 'b'
        elif message == '&':
            message = 'c'
        elif message == 'z':
            message = 'd'
        elif message == 'à':
            message = 'e'
        elif message == '@':
            message = 'f'
        elif message == ')':
            message = 'g'
        elif message == '8-':
            message = 'h'
        elif message == '<':
            message = 'i'
        elif message == '>':
            message = 'j'
        elif message == '$':
            message = 'k'
        elif message == 'é':
            message = 'l'
        elif message == 'r':
            message = 'm'
        elif message == '_':
            message = 'n'
        elif message == '-':
            message = 'o'
        elif message == 'è':
            message = 'p'
        elif message == '*':
            message = 'q'
        elif message == '*/':
            message = 'r'
        elif message == '+4':
            message = 's'
        elif message == '0.':
            message = 't'
        elif message == '4-p':
            message = 'u'
        elif message == 'ç':
            message = 'v'
        elif message == '*-+':
            message = 'w'
        elif message == '+-':
            message = 'x'
        elif message == '-+':
            message = 'y'
        elif message == '0.0':
            message = 'z'
        
        elif message == '+6-.':
            message = 'é'
        elif message == '@ù':
            message = 'è'
        elif message == '.*.+':
            message = 'à'
        elif message == '^14-+.^':
            message = 'ç'

        elif message == 'x0x':
            message = '0'
        elif message == './':
            message = '1'
        elif message == '+à':
            message = '2'
        elif message == '--++':
            message = '3'
        elif message == '+(-':
            message = '4'
        elif message == '3.20':
            message = '5'
        elif message == '<5-':
            message = '6'
        elif message == '+2./':
            message = '7'
        elif message == '-à.-':
            message = '8'
        elif message == '++9.0':
            message = '9'
        elif message == '+.+':
            message = ' '
        elif message == '-.-':
            message = ','
        elif message == '*-*':
            message = '.'
        elif message == '-*-':
            message = '('
        elif message == '_-_':
            message = ')'
        elif message == '-_-':
            message = ':'
        elif message == ':)':
            message = ';'
        elif message == ':(':
            message = '!'
        elif message == ':D':
            message = '?'
        elif message == ':*':
            message = '-'
        elif message == ':p':
            message = '_'

        DecryptedString+=message

    output = open("result", 'a')
    output.write('========')
    output.write('\n')
    output.write("Text : " + str(imo) + '\n')
    output.write("Cypher : " + str(DecryptedString) + '\n')
    output.write('========\n\n')
    output.close()

    print("Clear String : ", clearString)
    print("Decrypted String : ", DecryptedString)



decrypt()