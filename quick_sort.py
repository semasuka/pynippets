"""Implement quick sort in Python.
Input a list.
Output a sorted list."""
from random import randint

def gen_list(size=10,max=100):
    return [randint(0,max) for _ in range(size)]

def sort_list(words):
    if len(words) <= 1:
        return words
    smaller,equal,larger = [],[],[]
    pivot = words[randint(0, len(words) - 1)]

    for i in words:
        if i < pivot:
            smaller.append(i)
        elif i == pivot:
            equal.append(i)
        else:
            larger.append(i)

    return sort_list(smaller)+equal+sort_list(larger)

# the_list = gen_list()
# print("unsorted ",the_list)
# sorted_list = sort_list(the_list)
# print("sorted ",sorted_list)

print(sort_list(["u", "xe", "f", "ghijkl"]))