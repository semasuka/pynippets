"""
implementation of the selection sort
"""
from random import randint
def gen_list(size=10,max=100):
    return [randint(0,max) for _ in range(size)]

def selection_sort(the_list):
    sorted_len = 0
    while sorted_len < len(the_list):
        min_index = None
        for i,element in enumerate(the_list[sorted_len:]):
            if min_index == None or element<the_list[min_index]:
                min_index = i+sorted_len
        the_list[sorted_len],the_list[min_index] = the_list[min_index],the_list[sorted_len]
        sorted_len += 1
    return the_list



the_list = gen_list()
print(the_list)
sorted_list = selection_sort(the_list)
print(sorted_list)