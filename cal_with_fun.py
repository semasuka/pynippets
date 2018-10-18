"""
Move the first letter of each word to the end of it, then add "ay" to the end of the word. Leave punctuation marks untouched.

Examples
pig_it('Pig latin is cool') # igPay atinlay siay oolcay
pig_it('Hello world !')     # elloHay orldway !
"""
import string
the_punctuation = list(string.punctuation)

def pig_it(text):
    final_string = ""
    for word in text.split():
        if word[0] not in the_punctuation:
            first_char = word[0]
            final_string += word[1:]
            final_string += first_char+"ay "
        else:
            final_string += word
    return final_string.strip()

print(pig_it("Hello world !"))
