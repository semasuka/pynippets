# """
# In some countries of former Soviet Union there was a belief about lucky tickets. A transport ticket of any sort was believed to posess luck if sum of digits on the left half of its number was equal to the sum of digits on the right half. Here are examples of such numbers:
#
# 003111    #             3 = 1 + 1 + 1
# 813372    #     8 + 1 + 3 = 3 + 7 + 2
# 17935     #         1 + 7 = 3 + 5  // if the length is odd, you should ignore the middle number when adding the halves.
# 56328116  # 5 + 6 + 3 + 2 = 8 + 1 + 1 + 6
# Such tickets were either eaten after being used or collected for bragging rights.
#
# Your task is to write a funtion luck_check(str), which returns true/True if argument is string decimal representation of a lucky ticket number, or false/False for all other numbers. It should throw errors for empty strings or strings which don't represent a decimal number.
# """
def is_it_luck_func(string,the_len):
    is_it_lucky = False
    middle = the_len//2
    part_1_sum = 0
    part_2_sum = 0
    for num in string[:middle]:
        part_1_sum += int(num)
    for num in string[middle:]:
        part_2_sum += int(num)
    #print(middle)
    if part_1_sum == part_2_sum:
        is_it_lucky = True
    return is_it_lucky

def luck_check(string):

    if not string.isdigit():
        raise Exception("the string is not a digit")
    else:
        the_len = len(string)

        #if it is an odd num
        if the_len%2==0:
            return is_it_luck_func(string,the_len)

        #if it is an even num
        else:
            middle_num_index = (the_len-1)//2
            string = list(string)
            del string[middle_num_index]
            string = "".join(string)
            return is_it_luck_func(string,the_len)

print(luck_check("6428"))
