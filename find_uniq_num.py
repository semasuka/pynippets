"""
There is an array with some numbers. All numbers are equal except for one. 
Try to find it!

findUniq([ 1, 1, 1, 2, 1, 1 ]) === 2
findUniq([ 0, 0, 0.55, 0, 0 ]) === 0.55
It’s guaranteed that array contains more than 3 numbers.

The tests contain some very huge arrays, so think about performance.

This is the first kata in series:

Find the unique number (this kata)
Find the unique string
Find The Unique
"""
import operator
def find_uniq(arr):
    first_char = arr[0]
    second_char = arr[1]
    third_char = arr[2]
    first_chars_list = []
    first_chars_list.extend([first_char,second_char,third_char])

    #print(first_chars_list)
    seen = {}
    dupes = []

    for x in first_chars_list:
        if x not in seen:
            seen[x] = 1
        else:
            if seen[x] == 1:
                dupes.append(x)
            seen[x] += 1
    repeated_num = max(seen.items(), key=operator.itemgetter(1))[0]
    #print(repeated_num)
    no_repeat = list(set(arr))
    #print(no_repeat)
    the_number = 0
    for i in no_repeat:
        if i != repeated_num:
            the_number = i
    return the_number
print(find_uniq([ 3, 10, 3, 3, 3 ]))