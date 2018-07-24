"""
Write a function that takes in a string of one or more words, and 
returns the same string, but with all five or more letter words 
reversed (Just like the name of this Kata). Strings passed in will 
consist of only letters and spaces. Spaces will be included only 
when more than one word is present.


Examples:

spinWords( "Hey fellow warriors" ) => returns "Hey wollef sroirraw" 
spinWords( "This is a test") => returns "This is a test" 
spinWords( "This is another test" )=> returns "This is rehtona test"

"""

def spin_words(sentence):
    sentence_list = []
    for word in sentence.split(" "):
        sentence_list.append(word)
    char_count = 0

    sentence_list_final = []
    for word in sentence_list:
        for char in word:
            char_count+=1
        if char_count >= 5:
            sentence_list_final.append(word[::-1])
        else:
            sentence_list_final.append(word)
        char_count = 0

    #print(sentence_list_final)
    final_sentence = str(sentence_list_final[0])
    if len(sentence_list_final) >= 2:
        for word in sentence_list_final[1:-1]:
            final_sentence += " "+word
        final_sentence += " "+str(sentence_list_final[-1])
    
    return final_sentence




print(spin_words("Welcome"))