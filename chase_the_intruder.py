"""
You are given an array (which will have a length of at least 3, 
but could be very large) containing integers. The array is either 
entirely comprised of odd integers or entirely comprised of even integers 
except for a single integer N. Write a method that takes the array 
as an argument and returns this "outlier" N.
"""

def find_outlier(integers):
    odd_count = 0
    even_count = 0
    the_intruder = 0
    for digit in integers:
        if digit%2 == 0:
            odd_count+=1
        else:
            even_count+=1
    if even_count > odd_count:
        for digit in integers:
            if digit%2 == 0:
                the_intruder = digit
    else:
        for digit in integers:
            if digit%2 != 0:
                the_intruder = digit
    return the_intruder

print(find_outlier([160, 3, 1719, 19, 11, 13, -21]))