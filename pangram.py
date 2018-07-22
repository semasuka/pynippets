"""
A pangram is a sentence that contains every single letter of the alphabet at least once. 
For example, the sentence "The quick brown fox jumps over the lazy dog" is a pangram, 
because it uses the letters A-Z at least once (case is irrelevant).

Given a string, detect whether or not it is a pangram. Return True if it is, False if 
not. Ignore numbers and punctuation.
"""
import string
def is_pangram(the_string):

    #removing all special character in the string
    the_string = "".join(e for e in the_string if e.isalnum())
    #removing all the number
    the_string = "".join(i for i in the_string if not i.isdigit())
    #put it i set to remove all the duplicated
    the_string_list = set()

    for word in the_string:
        for char in word:
            the_string_list.add(char.lower())

    print(sorted(the_string_list))
    all_char = list(string.ascii_lowercase)
    print(all_char)
    #if all the ascii char in the string
    if all(char in the_string_list for char in all_char):
        return True
    else:
        return False

print(is_pangram("The quick, brown fox jumps over the lazy dog!"))