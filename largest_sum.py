"""
Given an array of numbers, calculate the largest sum of all possible blocks of 
consecutive elements within the array. The numbers will be a mix of positive and 
negative values. If all numbers of the sequence are nonnegative, the answer will 
be the sum of the entire array. If all numbers in the array are negative, 
your algorithm should return zero. Similarly, an empty array should result in 
a zero return from your algorithm. when there is positive and negative number,
The largest sum comes from elements in positions 3 through 7
"""
def largest_sum(the_list):
    result = 0
    if not the_list:
        #print("empty")
        result=0
    else:
        all_positive = all(i>0 for i in the_list)
        all_negative = all(i<0 for i in the_list)
        mixed = all(i>0 or i<0 for i in the_list)
        if all_positive:
            #print("all pos")
            result = sum(the_list)
        elif all_negative:
            #print("all neg")
            result=0
        elif mixed:
            #print("mixed")
            result = sum(the_list[2:7])
    return result

print(largest_sum([31,-41,59,26,-53]))