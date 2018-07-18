import collections

def duplicate_count(text):
    print [item for item, count in collections.Counter(text).items() if count > 1]
    #dupl_char = []
    #check if it is the last iteration
    # last = len(text) - 1
    # for i,char in enumerate(text):
    #     while  i!= last:
    #         if text[i] == text[i+1]:
    #             dupl_char.append(char)
    # print(*dupl_char)






duplicate_count("indivisibility")