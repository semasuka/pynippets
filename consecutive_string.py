"""
return the k consecutive longuest string
"""
def longest_consec(strarr, k):
    long_first_word=[]
    concat_word = ""
    strarr.sort(key=len,reverse=False)
    if k <= 0:
        for word in strarr[:k]:
            long_first_word.append(word)
        
        for word in long_first_word:
            concat_word += word

        print(concat_word)
    else:
        return ""








longest_consec(["wlwsasphmxx","owiaxujylentrklctozmymu","wpgozvxxiu"], 2)