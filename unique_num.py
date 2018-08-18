"""
There is an array with some numbers. All numbers are equal except for one. Try to find it!

findUniq([ 1, 1, 1, 2, 1, 1 ]) === 2
findUniq([ 0, 0, 0.55, 0, 0 ]) === 0.55
It’s guaranteed that array contains more than 3 numbers.

The tests contain some very huge arrays, so think about performance.
"""
def find_uniq(arr):
    set_arr = list(set(arr))
    first_num = set_arr[0]
    second_num = set_arr[1]
    first_num_count = 0
    second_num_count = 0
    for num in arr:
        if num == first_num:
            first_num_count+=1
        elif num == second_num:
            second_num_count+=1
    if first_num_count > second_num_count:
        return second_num
    else:
        return first_num

print(find_uniq([ 1, 1, 1, 2, 1, 1 ]))
