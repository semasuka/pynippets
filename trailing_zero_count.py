"""
Write a program that will calculate the number of trailing zeros in a factorial of a given number.

N! = 1 * 2 * 3 * ... * N

Be careful 1000! has 2568 digits...

For more info, see: http://mathworld.wolfram.com/Factorial.html

Examples
zeros(6) = 1
# 6! = 1 * 2 * 3 * 4 * 5 * 6 = 720 --> 1 trailing zero

zeros(12) = 2
# 12! = 479001600 --> 2 trailing zeros
Hint: You're not meant to calculate the factorial. Find another way to find the number of zeros.
"""
import math
def zeros(n):
    the_fact = str(math.factorial(n))
    reversed_fact = the_fact[::-1]
    zero_count = 0
    for char in reversed_fact:
        if char == "0":
            zero_count+=1
        else:
            break
    return zero_count


print(zeros(134))