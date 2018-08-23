
from random import randint

def gen_list(size=10,max=100):
    return [randint(0,max) for _ in range(size)]
def insertion_sort(the_list):
    for sort_len in range(1,len(the_list)):
        #next element in the unsorted list
        cur_item = the_list[sort_len]
        #current index of item
        insert_index =  sort_len
        #iterate till we reach correct insert spot
        while insert_index>0 and cur_item<the_list[insert_index-1]:
            the_list[insert_index] = the_list[insert_index-1]
            insert_index-=1
        the_list[insert_index] = cur_item
    return the_list

the_list = gen_list()
print(the_list)
sorted_list = insertion_sort(the_list)
print(sorted_list)