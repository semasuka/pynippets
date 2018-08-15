"""
Your job is to write a function which increments a string, to create a new string. If the string already ends with a number, the number should be incremented by 1. If the string does not end with a number the number 1 should be appended to the new string.

Examples:

foo -> foo1

foobar23 -> foobar24

foo0042 -> foo0043

foo9 -> foo10

foo099 -> foo100

Attention: If the number has leading zeros the amount of digits should be considered.
"""

def increment_string(strng):
    if len(strng)!=0:
        first_dig_index = 0
        if strng.isdigit():
            def add(x):
                return str(int(x) + 1).zfill(len(x))
            incre_the_num_part = add(strng)
            return incre_the_num_part
        else:
            for char in strng:
                if not char.isalpha():
                    first_dig_index = strng.index(char)
                    break


            if first_dig_index != 0:
                the_num_part = strng[first_dig_index:]
                the_string_part = strng[:first_dig_index]
                def add(x):
                    return str(int(x) + 1).zfill(len(x))
                incre_the_num_part = add(the_num_part)
                result = the_string_part + incre_the_num_part
                return result
            else:
                return strng+"1"
    else:
        return "1"
print(increment_string("(49\\BL9g/j856283517C'860=+g+19026157(3487774000000006"))
