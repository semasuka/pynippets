"""
A Narcissistic Number is a number which is the sum of its own digits, each raised to the power of the number of digits.

For example, take 153 (3 digits):

    1^3 + 5^3 + 3^3 = 1 + 125 + 27 = 153
and 1634 (4 digits):

    1^4 + 6^4 + 3^4 + 4^4 = 1 + 1296 + 81 + 256 = 1634
"""
def narcissistic(number):
    num_list = list(str(number))
    num_len = len(num_list)
    #print(num_list)
    #print(num_len)
    total = 0
    for the_num in num_list:
        total+=(int(the_num))**num_len
    #print(total)
    if number == total:
        return True
    else:
        return False

print(narcissistic(9800817))