"""
Write a function that calculates the least common multiple of its arguments; each argument is assumed to be a non-negative integer. In the case that there are no arguments (or the provided array in compiled languages is empty), return 1.



"""
from math import gcd
def lcm(*args):
    the_list = list(args)
    the_lcm = the_list[0]
    for i in the_list[1:]:
        the_lcm = the_lcm*int(i/gcd(the_lcm,i))
    print(the_lcm)


lcm(2,5)