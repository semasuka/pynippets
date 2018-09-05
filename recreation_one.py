"""
Divisors of 42 are : 1, 2, 3, 6, 7, 14, 21, 42. These divisors squared are: 1, 4, 9, 36, 49, 196, 441, 1764. The sum of the squared divisors is 2500 which is 50 * 50, a square!

Given two integers m, n (1 <= m <= n) we want to find all integers between m and n whose sum of squared divisors is itself a square. 42 is such a number.

The result will be an array of arrays or of tuples (in C an array of Pair) or a string, each subarray having two elements, first the number whose squared divisors is a square and then the sum of the squared divisors.

#Examples:

list_squared(1, 250) --> [[1, 1], [42, 2500], [246, 84100]]
list_squared(42, 250) --> [[42, 2500], [246, 84100]]
The form of the examples may change according to the language, see Example Tests: for more details.

Note

In Fortran - as in any other language - the returned string is not permitted to contain any redundant trailing whitespace: you can use dynamically allocated character strings.

"""
from functools import reduce
from math import sqrt

def factors(n):
    div_list = list(set(reduce(list.__add__,
                      ([i, n//i] for i in range(1, n + 1) if n % i == 0))))
    div_list_squared = []
    for i in div_list:
        div_list_squared.append(i*i)
    the_sum = sum(div_list_squared)
    return the_sum

def list_squared(m, n):
    num_between = list(range(m,n+1))
    #print(num_between)
    num_between_sum_div = []
    for i in num_between:
        num_between_sum_div.append(factors(i))
    #print(num_between_sum_div)
    #print(num_between_sum_div[41])
    squared_num = []
    squared_num_index = []
    for j in num_between_sum_div:
        if sqrt(j).is_integer():
            squared_num.append(j)
            the_num = num_between[num_between_sum_div.index(j)]
            squared_num_index.append(the_num)
    print(squared_num)
    print(squared_num_index)
    final = [list(x) for x in zip(squared_num_index,squared_num)]
    return final


print(list_squared(1430, 1680))

#print(factors(30))