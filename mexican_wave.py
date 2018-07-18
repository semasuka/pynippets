def elevated(the_str):
    return [ the_str[:i]+the_str[i].upper()+the_str[i+1:] for i in range(len(the_str)) if the_str[i].isalpha()]




#wave("codewars")
print(elevated("hello"))