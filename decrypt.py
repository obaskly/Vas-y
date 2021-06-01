#!/usr/bin/python
# -*- coding: utf-8 -*-
def decrypt():
    imo = str(input("Your message: "))
    sen = imo.lower()
   
    DecryptedString = ''
    clearString = sen
    for message in sen:

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
        elif message == '-':
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
