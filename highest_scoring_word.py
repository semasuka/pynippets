"""
Given a string of words, you need to find the highest scoring word.

Each letter of a word scores points according to it's position in the alphabet: a = 1, b = 2, c = 3 etc.

You need to return the highest scoring word as a string.

If two words score the same, return the word that appears earliest in the original string.

All letters will be lowercase and all inputs will be valid.
"""
def high(the_string):
    the_score_dic = {"a":1,'b':2,'c':3,'d':4,'e':5,'f':6,'g':7,'h':8,'i':9,'j':10,'k':11,'l':12,'m':13,'n':14,'o':15,'p':16,'q':17,'r':18,'s':19,'t':20,'u':21,'v':22,'w':23,'x':24,'y':25,'z':26}
    the_score_count = 0
    the_score_list = []
    the_string_list = []
    the_string = the_string.replace(" ",",")
    for word in the_string.split(","):
        the_string_list.append(word)
    for word in the_string_list:
        for char in word:
            for key,value in the_score_dic.items():
                if key == char:
                    the_score_count += value
        the_score_list.append(the_score_count)
        the_score_count = 0
    max_index_string = the_score_list.index(max(the_score_list)) 
    big_string = the_string_list[max_index_string]
    return big_string

print(high('what time are we climbing up the volcano'))