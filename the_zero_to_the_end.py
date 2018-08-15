"""
Write an algorithm that takes an array and moves all of the zeros to the end
preserving the order of the other elements.

move_zeros([false,1,0,1,2,0,1,3,"a"]) # returns[false,1,1,2,1,3,"a",0,0]
"""
def move_zeros(the_list):
    false_index = []
    #counting and storing the index of False occurence
    for count,element in enumerate(the_list):
        if element == 0:
            if element is False:
                false_index.append(count)
    if len(false_index) !=0:
        first_false = false_index[0]
        zero_count_before = 0
        for element in the_list[:first_false]:
            if element == 0:
                zero_count_before += 1

    zero_count = 0
    for element in the_list:
        if element == 0:
            if element is not False:
                zero_count += 1
                #removing all the 0
                the_list = list(filter(lambda a: a != 0, the_list))

    #adding zeros at the end
    for i in range(zero_count):
        the_list.append(0)
    #adding False that have been previously removed with zeros
    
    for index in false_index:
        the_list.insert(index-zero_count_before,False)
    return the_list

print(move_zeros([9, 9, 0, 'x', False, 0, 0, -6, -4, 0, -5, 'a', 'a', -10, '0', 1, 9, 'a', 10, -2, 6, 'x', False, 'c', 2, 1, -2, 'string', -5, 10, 9, True, 0, 2, 5, True, 0, -7])) 
