"""
Write a function toWeirdCase (weirdcase in Ruby) that accepts a string, 
and returns the same string with all even indexed characters in each 
word upper cased, and all odd indexed characters in each word lower cased. 
The indexing just explained is zero based, so the zero-ith index is even, 
therefore that character should be upper cased.

The passed in string will only consist of alphabetical characters and 
spaces(' '). Spaces will only be present if there are multiple words. 
Words will be separated by a single space(' ').

Examples:
to_weird_case('String'); # => returns 'StRiNg'
to_weird_case('Weird string case') # => returns 'WeIrD StRiNg CaSe'
"""
def to_weird_case(the_string):
    the_string_weird = ""
    the_string_list = []
    #removing all the white space first
    for word in the_string.split(" "):
        the_string_list.append(word)
    
    for word in the_string_list:
        for count,char in enumerate(word):
            #for even index
            if count%2 == 0:
                the_string_weird += char.upper()
            else:
                the_string_weird += char.lower()

        the_string_weird+= " "
    #removing the last white space 
    the_string_weird = the_string_weird.strip()
    return the_string_weird


print(to_weird_case('Weird string case'))