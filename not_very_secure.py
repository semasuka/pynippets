"""
In this example you have to validate if a user input string is alphanumeric. The given string is not nil, so you don't have to check that.

The string has the following conditions to be alphanumeric:

At least one character ("" is not valid)
Allowed characters are uppercase / lowercase latin letters and digits from 0 to 9
No whitespaces/underscore


"""
def alphanumeric(the_string):
    if len(the_string) == 0:
        return False
    else:
        is_alpha = False
        alnum_count = 0
        for char in the_string:
            if char.isalnum():
                alnum_count+=1
        if alnum_count == len(the_string):
            is_alpha = True
        return is_alpha



alphanumeric("")