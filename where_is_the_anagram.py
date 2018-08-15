"""
What is an anagram? Well, two words are anagrams of each other if they 
both contain the same letters. For example:

'abba' & 'baab' == true

'abba' & 'bbaa' == true

'abba' & 'abbba' == false
Write a function that will find all the anagrams of a word from a list. 
You will be given two inputs a word and an array with words. 
You should return an array of all the anagrams or an empty array 
if there are none. For example:

anagrams('abba', ['aabb', 'abcd', 'bbaa', 'dada']) => ['aabb', 'bbaa']

anagrams('racer', ['crazer', 'carer', 'racar', 'caers', 'racer']) => 
['carer', 'racer']

anagrams('laser', ['lazing', 'lazy',  'lacer']) => []
"""
def anagrams(the_word,all_words):
    all_words_sorted = []
    for word in all_words:
        all_words_sorted.append(sorted(word))

    the_word_sorted = "".join(sorted(the_word))
    the_word_list = []
    for char in the_word_sorted:
        the_word_list.append(char)

    index_list = []
    for count,word in enumerate(all_words_sorted):
        if word == the_word_list:
            index_list.append(count)

    final_list = []
    for index in index_list:
        final_list.append(all_words[index])
    return final_list



anagrams('abba', ['aabb', 'abcd', 'bbaa', 'dada'] )