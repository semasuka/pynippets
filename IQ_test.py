"""
to find out which one of the given numbers differs from the others in a list
"""
def iq_test(numbers):
    num_list = []
    numbers = numbers.replace(" ",",")
    for i in numbers.split(","):
        #if i != ",":
        num_list.append(int(i))
            #while numbers.find(i+1) != ",":


    num_list_even = []
    num_list_odd = []
    for i in num_list:
        if i%2 == 0:
            num_list_even.append(i)
        else:
            num_list_odd.append(i)


    if len(num_list_even) > len(num_list_odd):
        num_odd_str = str(num_list_odd[0])
        #print(len(numbers))
        for char in numbers:
            if char == num_odd_str:
                if numbers[0] == num_odd_str:
                    the_index_str_with_white = numbers.find(char)+1
                    return the_index_str_with_white
                else:
                    the_index_str_with_white = numbers.find(char)
                    numbers = numbers.replace(","," ")
                    no_whitespace = whitespace_count(numbers,the_index_str_with_white)
                    index = the_index_str_with_white - no_whitespace
                    return index
    else:
        num_even_str = str(num_list_even[0])
        for char in numbers:
            if char == num_even_str:
                if numbers[0] == num_even_str:
                    the_index_str_with_white = numbers.find(char)+1
                    return the_index_str_with_white
                else:
                    the_index_str_with_white = numbers.find(char)
                    numbers = numbers.replace(","," ")
                    no_whitespace = whitespace_count(numbers,the_index_str_with_white)
                    index = the_index_str_with_white - no_whitespace
                    return index

def whitespace_count(numbers,k):
    whitespace_counter = 0
    for char in numbers[:k]:
        if char == " ":
            whitespace_counter+=1
    return whitespace_counter-1


iq_test("1 2 2")
#whitespace_count("2 4 7 8 10",4)