"""
An Arithmetic Progression is defined as one in which there is a constant difference 
between the consecutive terms of a given series of numbers. You are provided with 
consecutive elements of an Arithmetic Progression. There is however one hitch: 
exactly one term from the original series is missing from the set of numbers 
which have been given to you. The rest of the given series is the same as the 
original AP. Find the missing term.

You have to write the function findMissing(list), list will always be at least 
3 numbers. The missing term will never be the first or last one.

Example
find_missing([1, 3, 5, 9, 11]) == 7
```

PS: This is a sample question of the facebook engineer challenge on interviewstreet. 
I found it quite fun to solve on paper using math, derive the algo that way. 
Have fun!
"""
def find_missing(sequence):
    first_interval = sequence[1]-sequence[0]
    second_interval = sequence[2]-sequence[1]
    real_interval = 0
    missing_num = 0
    if first_interval > second_interval:
        real_interval = second_interval
    else:
        real_interval = first_interval
    for digit in sequence:
        if digit+real_interval != sequence[sequence.index(digit)+1]:
            missing_num = digit+real_interval
            break
    return missing_num

find_missing([1, 3, 4, 5, 6, 7, 8, 9])