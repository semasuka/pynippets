"""
Given a number, return a string with dash'-'marks before and after each odd integer, 
but do not begin or end the string with a dash mark.

Ex:

dashatize(274) -> '2-7-4'
dashatize(6815) -> '68-1-5'
"""

def dashatize(num):
    # get 'em
    #for char in str(num[1]):
    final_string = ""
    num_list = []
    for digit in str(num):
        num_list.append(int(digit))
    print(num_list)
    if num_list[0] != "-":
        for num in num_list[1:]:
            if num%2 != 0:
                final_string += "-"+str(num)+"-"
            else:
                final_string += str(num)
            

    # elif num_list[0] == "-":
    #         del num_list[0]
    #         if num%2 != 0:
    #             final_string += "-"+str(num)+"-"
    #         else:

    #             final_string += str(num)
    final_string = str(num_list[0])+final_string
    print(final_string)




dashatize(9743000443322)