"""
Write simple .camelCase method (camel_case function in PHP, CamelCase in C# or 
camelCase in Java) for strings. All words must have their first letter capitalized 
without spaces.

For instance:

camelcase("hello case") => HelloCase
camelcase("camel case word") => CamelCaseWord
Don't forget to rate this kata! Thanks :)
"""

def camel_case(sentence):
    #removing white space in front and back
    sentence = sentence.strip()
    #removing the white space and place in the list
    sentence = sentence.split()
    sentence_cap = ""
    for word in sentence:
        sentence_cap += word.capitalize()
    return sentence_cap

camel_case(" camel case word")