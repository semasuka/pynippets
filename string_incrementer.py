"""
Your job is to write a function which increments a string, to create a new string. 
If the string already ends with a number, the number should be incremented by 1. 
If the string does not end with a number the number 1 should be appended to the new string


Examples:

foo -> foo1

foobar23 -> foobar24

foo0042 -> foo0043

foo9 -> foo10

foo099 -> foo100

Attention: If the number has leading zeros the amount of digits should be considered.
"""
import string
def increment_string(the_string):
    the_string_final = ""
    the_punctuation = string.punctuation
    first_digit_index = 0
    #print("last element ",the_string[-1])
    last_digit_index = the_string.index(the_string[-1])
    print(last_digit_index)
    if the_string == "":
        return 1
    else:
        if the_string[-1].isdigit():
            for count,char in enumerate(the_string):
                if char.isdigit():
                    first_digit_index = count
                    break
            print("index of the first digit ",count)
            print("index of the last digit ",last_digit_index)
            if last_digit_index == count:
                the_string_final += the_string[:-1] + str(int(the_string[-1])+1)
            elif last_digit_index != count:
                #first part where there is no digit
                the_string_final += the_string[:first_digit_index]
                #the second part where there is digit only
                the_num_part = int(the_string[first_digit_index:last_digit_index+1])+1
                zfill_len = (last_digit_index - first_digit_index)+1
                the_num_part = str(the_num_part).zfill(zfill_len)
                #increamenting by one
                the_string_final += the_num_part
                #print(the_string_final)
        elif the_string[-1].isalpha() or the_string[-1] in the_punctuation:
            the_string_final += the_string+"1"
        return the_string_final



print(increment_string("foobar099"))
