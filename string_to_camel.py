"""
Complete the method/function so that it converts dash/underscore delimited 
words into camel casing. The first word within the output should be capitalized 
only if the original word was capitalized.

Examples
to_camel_case("the-stealth-warrior") # returns "theStealthWarrior"

to_camel_case("The_Stealth_Warrior") # returns "TheStealthWarrior"
"""
def to_camel_case(text):
    words = []
    words_cap = []
    final_word = ""
    #checking if the string is empty
    if not text:
        return ""
    #if not
    else:
        for char in text:
            #replacing all the "-"" by ","
            if char == "-":
                text = text.replace("-",",")
            #replacing all the "_" by ","
            if char == "_":
                text = text.replace("_",",")
        #put all the words(separated by ,) in the list
        for char in text:
            for word in text.split(","):
                words.append(word)
            break
        #capitalize all the elements in the list except the first one
        for word in words[1:]:
            words_cap.append(word.capitalize())
        #first adding the first word to the string
        for char in words:
            final_word+=words[0]
            break
        #adding the reminding words to the string
        for word_cap in words_cap:
            final_word+=word_cap
        return final_word

print(to_camel_case(""))