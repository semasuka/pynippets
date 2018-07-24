"""
Your friend won't stop texting his girlfriend. It's all he does. 
All day. Seriously. The texts are so mushy too! The whole situation 
just makes you feel ill. Being the wonderful friend that you are, 
you hatch an evil plot. While he's sleeping, you take his phone and 
change the autocorrect options so that every time he types "you" or "u" 
it gets changed to "your sister."

Write a function called autocorrect that takes a string and replaces all 
instances of "you" or "u" (not case sensitive) with "your sister" 
(always lower case).

Return the resulting string.

Here's the slightly tricky part: These are text messages, so there are 
different forms of "you" and "u".

For the purposes of this kata, here's what you need to support:

"youuuuu" with any number of u characters tacked onto the end
"u" at the beginning, middle, or end of a string, but NOT part of a word
"you" but NOT as part of another word like youtube or bayou
"""

def autocorrect(the_string):
    if len(the_string) == 0:
        return False
    else:
        the_string_list = []
        the_final_string = ""
        for word in the_string.split(" "):
            the_string_list.append(word)
        if len(the_string_list) == 1:
            for word in the_string_list:
                try:
                    if word.lower() == "u" or word.lower() == "you" or word[0].lower() == "y" and word[1].lower() == "o" and word[2].lower() == "u" and word[3].lower() == "u":
                        return "your sister"
                except IndexError:
                    return word
                else:
                    return word
        else:
            for count,word in enumerate(the_string_list):
                if word == "u" or word == "you":
                    the_string_list[count] = "your sister"
                if len(word) >=4:
                    if word[0] == "y" and word[1] == "o" and word[2] == "u" and word[3] == "u":
                        the_string_list[count] = "your sister"
            for word in the_string_list:
                the_final_string += " "+word
            the_final_string = the_final_string.strip()
            return the_final_string
print(autocorrect("youtube"))