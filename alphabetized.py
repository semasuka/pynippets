"""
Re-order the characters of a string, so that they are concatenated into 
a new string in "case-insensitively-alphabetical-order-of-appearance" order. 
space and punctuation shall simply be removed!

The input is restricted to contain no numerals and only words containing 
the english alphabet letters.

Example:

alphabetized("The Holy Bible") # "BbeehHilloTy"
"""

def alphabetized(the_string):
    the_string = ''.join(e for e in the_string if e.isalnum())
    if len(the_string) == 0:
        return ""
    else:
        the_string = sorted(the_string, key=lambda s: s.casefold())
        final_string = ""
        for char in the_string:
            final_string += char
        return final_string


print(alphabetized(""))