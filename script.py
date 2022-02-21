#!/usr/bin/python

import sys


def encypt_func(txt, s):

    result = ""

# transverse the plain txt
    for i in range(len(txt)):
        char = txt[i]
        # encypt_func uppercase characters in plain txt

        if (char.isupper()):
            result += chr((ord(char) + s - 65) % 26 + 65)
        # encypt_func lowercase characters in plain txt
        elif(char.islower()):
            result += chr((ord(char) + s - 97) % 26 + 97)

    return result


LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
txt = "CEASER MAN is bad"
s = 4
num = 26-s

encrypt_word = sys.argv[1]

result = encypt_func(encrypt_word, s)
print(" The encrypted text is: "+result)
