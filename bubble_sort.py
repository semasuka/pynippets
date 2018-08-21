"""
implementation of bubble sort
"""

from random import randint

def gen_list(size=10,max=100):
    return [randint(0,max) for _ in range(size)]

def bubble_sort(the_list):
    swapped = True
    while swapped:
        swapped = False
        for i in range(1,len(the_list)):
            if the_list[i-1] > the_list[i]:
                the_list[i-1],the_list[i] = the_list[i],the_list[i-1]
                swapped = True

    return the_list



the_list = gen_list()
print(the_list)
sorted_list = bubble_sort(the_list)
print(sorted_list)