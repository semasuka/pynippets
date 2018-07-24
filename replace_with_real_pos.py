"""
Welcome.

In this kata you are required to, given a string, replace every letter 
with its position in the alphabet.

If anything in the text isn't a letter, ignore it and don't return it.

a being 1, b being 2, etc.

As an example:

alphabet_position("The sunset sets at twelve o' clock.")
Should return "20 8 5 19 21 14 19 5 20 19 5 20 19 1 20 20 23 5 12 22 5 
15 3 12 15 3 11" as a string.
"""

def alphabet_position(text):
    #removing all the special character
    the_string = "".join(e for e in text if e.isalnum()).lower()
    #dic for char and value
    char_and_val = {'a':1, 'b':2, 'c':3, 'd':4, 'e':5, 'f':6, 'g':7, 'h':8, 'i':9, 'j':10, 'k':11, 'l':12, 'm':13, 'n':14, 'o':15, 'p':16, 'q':17, 'r':18, 's':19, 't':20, 'u':21, 'v':22, 'w':23, 'x':24, 'y':25, 'z':26}
    print(the_string)
    final_string = ""
    for char in the_string:
        for key,value in char_and_val.items():
            if key == char:
                final_string+= " "+str(value)
    final_string = final_string.strip()
    return final_string

alphabet_position("The sunset sets at twelve o' clock.")