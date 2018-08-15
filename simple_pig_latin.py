"""
Move the first letter of each word to the end of it, then 
add "ay" to the end of the word. Leave punctuation marks untouched.

Examples
pig_it('Pig latin is cool') # igPay atinlay siay oolcay
pig_it('Hello world !')     # elloHay orldWay !

"""
import string
def pig_it(the_string):
    the_string_list = []
    the_string_changed_list = []
    the_string_changed = ""
    for char in the_string.split(" "):
        the_string_list.append(char)
    for word in the_string_list:
        if len(word) == 1 and word in string.punctuation:
            the_string_changed_list.append(word)
        else:
            for char in word:
                the_string_changed_list.append(word[1:]+word[0]+"ay")
                break
    print(the_string_changed_list)
    for word in the_string_changed_list:
        the_string_changed += " "+word
    the_string_changed = the_string_changed.strip()
    return the_string_changed


print(pig_it('O tempora o mores !'))