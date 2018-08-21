"""Implement quick sort in Python.
Input a list.
Output a sorted list."""
from random import randint

def gen_list(size=10,max=100):
    return [randint(0,max) for _ in range(size)]

def sort_list(the_string):
    if len(the_string) <= 1:
        return the_string
    smaller,equal,larger = [],[],[]
    pivot = the_string[randint(0,len(the_string)-1)]

    for i in the_string:
        if i < pivot:
            smaller.append(i)
        elif i == pivot:
            equal.append(i)
        else:
            larger.append(i)

    return sort_list(smaller)+equal+sort_list(larger)

the_list = gen_list()
print("unsorted ",the_list)
sorted_list = sort_list(the_list)
print("sorted ",sorted_list)