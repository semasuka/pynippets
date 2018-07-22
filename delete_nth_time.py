"""
Enough is enough!
Alice and Bob were on a holiday. Both of them took many pictures of the places 
they've been, and now they want to show Charlie their entire collection. 
However, Charlie doesn't like this sessions, since the motive usually repeats.
\He isn't fond of seeing the Eiffel tower 40 times. He tells them that he will only 
sit during the session if they show the same motive at most N times. Luckily, 
Alice and Bob are able to encode the motive as a number. Can you help them to 
remove numbers such that their list contains each number only up to N times, 
without changing the order?

Task
Given a list lst and a number N, create a new list that contains each number 
of lst at most N times without reordering. For example if N = 2, and the 
input is [1,2,3,1,2,1,2,3], you take [1,2,3,1,2], drop the next [1,2] since 
this would lead to 1 and 2 being in the result 3 times, and then take 3, 
which leads to [1,2,3,1,2,3].

Example
  delete_nth ([1,1,1,1],2) # return [1,1]

  delete_nth ([20,37,20,21],1) # return [20,37,21]
"""
def delete_nth(the_list,max_output):
    # code here
    seen = {}
    dupes = []
    the_digit_to_delete = 0
    for digit in the_list:
        if digit not in seen:
            seen[digit] = 1
        else:
            if seen[digit] == 1:
                dupes.append(digit)
            seen[digit] +=1
    print(seen)
    the_digit_to_delete_count = 0
    for key,value in seen.items():
        if value > 1 and max_output <= value:
            the_digit_to_delete = key
            the_digit_to_delete_count = value

    for digit in the_list:
        if digit == the_digit_to_delete:
            index_first_digit = the_list.index(digit)
    no_digit_to_leave = the_digit_to_delete_count - max_output
    no_digit_to_leave_count = 0
    print(the_list)
    print("the digit to delete ",the_digit_to_delete)
    print("the no of digit to leave ",no_digit_to_leave)
    print("no of digit ",the_digit_to_delete_count)
    print("index ",index_first_digit)
    print("max ",max_output)
    the_list_last = []
    for digit in the_list:
        if digit == the_digit_to_delete:
            no_digit_to_leave_count+=1

            if no_digit_to_leave == no_digit_to_leave_count:
                index_from = the_list.index(digit)+max_output

            elif no_digit_to_leave <= no_digit_to_leave_count:
                for digit in the_list[index_from:]:
                    if digit == the_digit_to_delete:
                        the_list_last = list(filter((digit).__ne__,the_list))
            the_list = the_list[:index_from]+the_list_last
    print(the_list)

delete_nth([20,37,20,21], 1)