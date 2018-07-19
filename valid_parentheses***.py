"""
a function called that takes a string of parentheses, and determines if the order of the parentheses is valid. The function should return true if the string is valid, and false if it's invalid.
"""

def valid_parentheses(string_par):
    is_true_par = False
    open_par_count = 0
    close_par_count = 0

    if string_par == "":
        is_true_par = True
    else:
        for char in string_par:
            if char == "(":
                open_par_count+=1
            elif char == ")":
                close_par_count+=1

    print(open_par_count)
    print(close_par_count)
    couple_par_count = 0
    if open_par_count == close_par_count:
        for char_1 in string_par:
            if char_1 ==  "(":
                for char_2 in string_par[string_par.index(char_1)+1:]:
                    if char_2 == ")":
                        couple_par_count += 1
                        print("_--")
                        break
                    else:
                        break
    print(couple_par_count)
    # print(correct_couple_par)

    # if couple_par_count == correct_couple_par:
    #     is_true_par = True

    print(is_true_par)



valid_parentheses("hi())(")