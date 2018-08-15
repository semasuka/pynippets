"""
Write a function named firstNonRepeatingLetter† that takes a string input, and returns the first character that is not repeated 
anywhere in the string.

For example, if given the input 'stress', the function should return 't', 
since the letter t only occurs once in the string, and occurs first in the string.

As an added challenge, upper- and lowercase letters are considered the same character, 
but the function should return the correct case for the initial letter. 
For example, the input 'sTreSS' should return 'T'.

If a string contains all repeating characters, it should return the empty string ("").

† Note: the function is called firstNonRepeatingLetter for historical reasons, 
but your function should handle any Unicode character.

"""

def first_non_repeating_letter(the_string):

    if the_string != "":
        seen = {}
        dupes = []

        for x in the_string.lower():
            if x not in seen:
                seen[x] = 1
            else:
                if seen[x] == 1:
                    dupes.append(x)
                seen[x] +=1
        print(seen)
        for key,value in seen.items():
            if value == 1:
                for char_main in the_string:
                    if key == char_main.lower() and char_main.istitle():
                        return key.upper()
                    elif key == char_main.lower() and not char_main.istitle():
                        return key.lower()


        else:
            return ""
    else:
        return ""





print(first_non_repeating_letter("hello world, eh?"))

