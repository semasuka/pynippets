"""
 Enter a number and have the program generate a tribonacy sequence(like fibonacy but instead uses 3 numbers)
"""
list_given = []
def tribonacci(lim_trib,list_given):
    tribonacci_list = []
    a,b,c = map(float,list_given)

    for i in range(lim_fib):
        tribonacci_list.append(a)
        a, b, c = b, c,a+b+c
    return tribonacci_list

lim_fib = int(input("Enter the limit of the fibonacci"))

tribonacci(lim_fib,list_given)